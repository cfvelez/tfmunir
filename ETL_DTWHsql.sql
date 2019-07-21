
Insert into trading_summary (year, location_code, export_value, import_value)
SELECT year, location_code, SUM(export_value), SUM(import_value)
FROM trading 
GROUP BY year, location_code;

Insert into 
trading_location_export(year, location_code,location_partner_code, export_value)
SELECT year, location_code,location_partner_code, SUM(export_value)
FROM trading  
GROUP BY year, location_code,location_partner_code;

Insert into 
trading_location_import(year, location_code,location_partner_code, import_value)
SELECT year, location_code,location_partner_code, SUM(import_value)
FROM trading  
GROUP BY year, location_code,location_partner_code;


Insert into 
trading_product_export(year, location_code,product_code, export_value)
SELECT year, location_code,product_code, SUM(export_value)
FROM trading  
GROUP BY year, location_code,product_code;


Insert into 
trading_product_import(year, location_code,product_code, import_value)
SELECT year, location_code,product_code, SUM(import_value)
FROM trading  
GROUP BY year, location_code,product_code;

