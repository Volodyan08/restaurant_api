from django.db import models
from datetime import datetime
from choices import CHECK_TYPE, PRINTER_TYPE, CHECK_STATUS


class CreateDateTimeModel(models.Model):
    created = models.DateTimeField(verbose_name="Creation date and time", default=datetime.now)


class Printer(CreateDateTimeModel, models.Model):
    name = models.CharField(max_length=30)
    api_key = models.CharField(max_length=200)
    check_type = models.CharField(choices=CHECK_TYPE)
    point_id = models.IntegerField()


class Check(CreateDateTimeModel, models.Model):
    printer = models.ForeignKey(Printer, on_delete=models.CASCADE)
    type = models.CharField(choices=PRINTER_TYPE)
    order = models.JSONField()
    status = models.CharField(default=CHECK_STATUS.NEW, choices=CHECK_STATUS)
    pdf_file = models.FileField(default=0)
