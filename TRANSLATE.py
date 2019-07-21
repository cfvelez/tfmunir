#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 11:27:55 2019

@author: cfvelez
"""
import MySQLdb
from translate import Translator

def connect_database():
    #Enter the values for you database connection
    dsn_database = "tmf"   # e.g. "MySQLdbtest"
    dsn_hostname = "localhost"       # e.g.: "mydbinstance.xyz.us-east-1.rds.amazonaws.com"
    dsn_port = 3306                        # e.g. 3306 
    dsn_uid = "root"             # e.g. "user1"
    dsn_pwd = ""            # e.g. "Password123"
    conn = MySQLdb.connect(host=dsn_hostname, port=dsn_port, user=dsn_uid, passwd=dsn_pwd, db=dsn_database)
    return conn

def translate_bd():
    translator= Translator(from_lang="english",to_lang="spanish")
    #cursor.execute("SELECT code, name_en FROM products WHERE code in ('01','22')")
    cursor.execute("SELECT code, name_en FROM locations")
    rows = cursor.fetchall()
    
    for row in rows:
        product = row[1]
        code = row[0]
        translation = translator.translate(product)
    
        #sql = "UPDATE products SET name_es = %s WHERE code = %s"
        sql = "UPDATE locations SET name_es = %s WHERE code = %s"
        val = (translation,code)
        #print(sql)
        try:
            cursor.execute(sql,val)
            conn.commit()
        except:
       # Rollback in case there is any error
           conn.rollback()

conn = connect_database()
cursor = conn.cursor()
translate_bd()
conn.close()
#translator= Translator(from_lang="english",to_lang="spanish")
#translation = translator.translate('Meat of horses, asses, mules and hinnies, fresh, chilled or frozen')  
#print(translation) 
           
