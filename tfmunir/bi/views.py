from django.shortcuts import render, HttpResponse
from bi.models import Locations, TradingSummary,TradingLocationExport
from bi.queries import Summary, ExportCountry, ImportCountry,ExportProduct, ImportProduct, correlationExports

# Create your views here.
def home(request):
    locations = Locations.objects.all()
    years = range(2016,1961,-1)
    contexto = {'locations':locations,'years':years}
    return render(request,'bi/base.html', contexto)

#Resumen general de importaciones y exportaciones
def view_summary(request):
    if request.method == 'GET':
        #Filtramos las variables
        country = request.GET.get('country', '')
        years_str = request.GET.get('years', '')
        years = years_str.split(',')
        
        #Obenter las importaciones y exportaciones
        data = Summary(country,years)

        return HttpResponse(data,content_type='application/json')

#Top 20 de exportaciones por pais por los años seleccionados
def view_country_export(request):
    if request.method == 'GET':
        #Filtramos las variables
        country = request.GET.get('country', '')
        years_str = request.GET.get('years', '')
        
        #Obenter el top 20 de exportaciones por pais.
        data = ExportCountry(country,years_str)
        return HttpResponse(data,content_type='application/json')

#Top 20 de importaciones por pais por los años seleccionados
def view_country_import(request):
    if request.method == 'GET':
        #Filtramos las variables
        country = request.GET.get('country', '')
        years_str = request.GET.get('years', '')
        
        #Obenter el top 20 de exportaciones por pais.
        data = ImportCountry(country,years_str)
        return HttpResponse(data,content_type='application/json')

#Top 20 de productos mas exportados
def view_product_export(request):
    if request.method == 'GET':
        #Filtramos las variables
        country = request.GET.get('country', '')
        years_str = request.GET.get('years', '')
        
        #Obenter el top 20 de los productos que mas se exportaron
        data = ExportProduct(country,years_str)
        return HttpResponse(data,content_type='application/json')

#Top 20 de productos mas importados
def view_product_import(request):
     if request.method == 'GET':
        #Filtramos las variables
        country = request.GET.get('country', '')
        years_str = request.GET.get('years', '')
        #Obenter el top 20 de los productos que mas se importaron
        data = ImportProduct(country,years_str)
        return HttpResponse(data,content_type='application/json')

# Test de correlaciòn exportaciones vs desempleo
def view_correlation_test(request):
     if request.method == 'GET':
        #Filtramos las variables
        country = request.GET.get('country', '')
        #Aplicar test de correlacion
        data = correlationExports(country)

        return HttpResponse(data,content_type='application/json')


