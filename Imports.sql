LOAD DATA LOCAL INFILE "/Users/cfvelez/ETL/imports/sitc_product.csv" INTO TABLE tmf.products
CHARACTER SET latin1
FIELDS TERMINATED BY '|'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(code,name_en,name_es);

LOAD DATA LOCAL INFILE "/Users/cfvelez/ETL/imports/locations.csv" INTO TABLE tmf.locations
FIELDS TERMINATED BY '|'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(code,name_en);

LOAD DATA LOCAL INFILE "/Users/cfvelez/ETL/imports/DesempleoWB.txt" INTO TABLE tmf.unemployment
FIELDS TERMINATED BY '|'
LINES TERMINATED BY '\n'
IGNORE 1 LINES
(location_name_es,location_code,year, value);

