from django.db import models

# Create your models here.

class Locations(models.Model):
    code = models.CharField(primary_key=True, max_length=4)
    name_en = models.CharField(max_length=32, blank=True, null=True)
    name_es = models.CharField(max_length=32, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'locations'


class Products(models.Model):
    code = models.CharField(primary_key=True, max_length=4)
    name_en = models.CharField(max_length=100, blank=True, null=True)
    name_es = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'products'


class Trading(models.Model):
    year = models.CharField(max_length=4, blank=True, null=True)
    product_code = models.CharField(max_length=6, blank=True, null=True)
    location_code = models.CharField(max_length=6, blank=True, null=True)
    location_partner_code = models.CharField(max_length=6, blank=True, null=True)
    export_value = models.FloatField(blank=True, null=True)
    import_value = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trading'


class TradingSummary(models.Model):
    year = models.CharField(max_length=4, blank=True, null=True)
    location_code = models.CharField(max_length=6, blank=True, null=True)
    export_value = models.FloatField(blank=True, null=True)
    import_value = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trading_summary'


class Unemployment(models.Model):
    location_name_es = models.CharField(max_length=100, blank=True, null=True)
    location_code = models.CharField(max_length=6, blank=True, null=True)
    year = models.CharField(max_length=4, blank=True, null=True)
    value = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'unemployment'

class TradingLocationExport(models.Model):
    year = models.CharField(max_length=4, blank=True, null=True)
    location_code = models.CharField(max_length=6, blank=True, null=True)
    location_partner_code = models.CharField(max_length=6, blank=True, null=True)
    export_value = models.FloatField(blank=True, null=True)
   

    class Meta:
        managed = False
        db_table = 'trading_location_export'


class TradingLocationImport(models.Model):
    year = models.CharField(max_length=4, blank=True, null=True)
    location_code = models.CharField(max_length=6, blank=True, null=True)
    location_partner_code = models.CharField(max_length=6, blank=True, null=True)
    import_value = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'trading_location_import'