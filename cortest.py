#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 13:51:12 2019

@author: cfvelez
"""

from scipy.stats import pearsonr
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

def getExport(country_code):
    cursor.execute("SELECT SUM(export_value) FROM trading_location_export WHERE year >='1991' AND location_code ='"+country_code+"' GROUP BY year ORDER BY year ASC")
    rows = cursor.fetchall()
    return rows

def getUnemployment(country_code):
    cursor.execute("SELECT  value FROM unemployment WHERE year <='2016' AND location_code ='"+country_code+"' ORDER BY year ASC")
    rows = cursor.fetchall()
    return rows

conn = connect_database()
cursor = conn.cursor()

list1 = getExport('COL')
print(len(list1))
list2 = getUnemployment('COL')
print(len(list2))
conn.close()
corr, p_value = pearsonr(list1, list2)
print( type(corr))
print(type(p_value))
