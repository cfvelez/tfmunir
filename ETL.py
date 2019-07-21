#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May 26 18:29:47 2019

@author: cfvelez
"""

import pandas
import MySQLdb
 

def connect_database():
    #Enter the values for you database connection
    dsn_database = "tmf"   # e.g. "MySQLdbtest"
    dsn_hostname = "localhost"       # e.g.: "mydbinstance.xyz.us-east-1.rds.amazonaws.com"
    dsn_port = 3306                        # e.g. 3306 
    dsn_uid = "root"             # e.g. "user1"
    dsn_pwd = ""            # e.g. "Password123"
    conn = MySQLdb.connect(host=dsn_hostname, port=dsn_port, user=dsn_uid, passwd=dsn_pwd, db=dsn_database)
    return conn

def load_bd(year, export_value, import_value,location_code,partner_code,sitc_product_code):
    sql = "insert into trading (year,export_value, import_value,location_code,location_partner_code,product_code) values('%s', '%d', '%d','%s','%s','%s')" % \
    (year, export_value, import_value,location_code,partner_code,sitc_product_code)
    #print(sql)
    try:
        cursor.execute(sql)
        conn.commit()
    except:
   # Rollback in case there is any error
       conn.rollback()
    
    
def etl(file):
    with open(file) as csv_file:
        data = pandas.read_csv(
                csv_file,
                usecols=['year', 'export_value', 'import_value','location_code','partner_code','sitc_product_code'],
                dtype={'year':str,'export_value':float, 'import_value':float,'location_code':str,'partner_code':str,'sitc_product_code':str }
                #nrows=20
                )
       # print(data.head(0))
        i = 0
        for row in data.itertuples(index=True, name='Pandas'):
            year = getattr(row, "year")
            export_value = getattr(row, "export_value")
            import_value = getattr(row, "import_value")
            location_code = getattr(row, "location_code")
            partner_code = getattr(row, "partner_code")
            sitc_product_code = getattr(row, "sitc_product_code")
            load_bd(year[:4], export_value, import_value,location_code,partner_code,sitc_product_code)
            i = i + 1
        print(i)

conn = connect_database()
cursor = conn.cursor()
etl('../home/country_partner_sitcproduct2digit_yearx.csv')
conn.close()




