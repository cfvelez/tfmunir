from bi.models import TradingSummary,TradingLocationExport, TradingLocationImport
from django.db.models import Avg, Count, Min, Sum
from django.core import serializers
from django.db import connection
from scipy.stats import pearsonr
import json

#Primer gráfico de lineas para las importaciones y exportaciones del pais seleccionado
def Summary(country,years):
        trading = TradingSummary.objects.values('year').filter(location_code=country, year__in=years).annotate(Sum("export_value"),Sum("import_value"))
        datos = json.dumps(list(trading))
        connection.close() 
        return datos

#Gráfico de barras para el top 20 de exportaciones por pais
def ExportCountry(country,years):
        with connection.cursor() as cursor:
                sql = "SELECT lc.name_es,sum(tle.export_value) export_value FROM trading_location_export  tle JOIN locations  lc ON lc.code = tle.location_partner_code WHERE tle.year IN ("+years+") AND tle.location_code='"+country+"' GROUP BY lc.name_es ORDER BY sum(tle.export_value) DESC LIMIT 0,19"
                cursor.execute(sql)
                row = cursor.fetchall()
                data = json.dumps(row)
                connection.close()
        return data

#Gráfico de barras para el top 20 de paises desde donde mas se importo
def ImportCountry(country,years):
        with connection.cursor() as cursor:
                sql = "SELECT lc.name_es,sum(tle.import_value) import_value FROM trading_location_import  tle JOIN locations  lc ON lc.code = tle.location_partner_code WHERE tle.year IN ("+years+") AND tle.location_code='"+country+"' GROUP BY lc.name_es ORDER BY sum(tle.import_value) DESC LIMIT 0,19"
                cursor.execute(sql)
                row = cursor.fetchall()
                data = json.dumps(row)
                connection.close()
        return data

#Gráfico de barras para el top 20 de productos que mas se exportaron
def ExportProduct(country,years):
        with connection.cursor() as cursor:
                sql = "SELECT pr.name_es,sum(tle.export_value) export_value FROM trading_product_export  tle JOIN products  pr ON pr.code = tle.product_code WHERE tle.year IN ("+years+") AND tle.location_code='"+country+"' GROUP BY pr.name_es ORDER BY sum(tle.export_value) DESC LIMIT 0,19"
                cursor.execute(sql)
                row = cursor.fetchall()
                data = json.dumps(row)
                connection.close()
        return data

#Gráfico de barras para el top 20 de productos que mas se importaron
def ImportProduct(country,years):
        with connection.cursor() as cursor:
                sql = "SELECT pr.name_es,sum(tle.import_value) import_value FROM trading_product_import  tle JOIN products  pr ON pr.code = tle.product_code WHERE tle.year IN ("+years+") AND tle.location_code='"+country+"' GROUP BY pr.name_es ORDER BY sum(tle.import_value) DESC LIMIT 0,19"
                cursor.execute(sql)
                row = cursor.fetchall()
                data = json.dumps(row)
                connection.close()
        return data

#Gráfico de dispersión para representar la relación desempleo exportaciones
def correlationExports(country):
        exports = []
        unemployment = []

        with connection.cursor() as cursor:
                sql = "SELECT SUM(export_value) FROM trading_location_export WHERE year >='1991' AND location_code='"+country+"' GROUP BY year ORDER BY year ASC"
                cursor.execute(sql)
                row = cursor.fetchall()
                exports = row

                sql = "SELECT value FROM unemployment WHERE year <='2016' AND location_code ='"+country+"' ORDER BY year ASC"
                cursor.execute(sql)
                row = cursor.fetchall()
                unemployment = row
                connection.close()

        points = []

        if (len(exports) == len(unemployment)):
                corr, p_value = pearsonr(exports, unemployment)

                for i in range(len(exports)):
                    point = {'x':unemployment[i][0],'y':exports[i][0]}
                    points.append(point)


                data = { "corr": corr[0], "p_value":p_value[0], "points":json.dumps(points) }
        else:
                data =  data = { "corr": 0, "p_value":0, "points":json.dumps(points) }

        
        return json.dumps(data, sort_keys=True, indent=3)