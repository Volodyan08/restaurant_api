from django.db import models


class Printer(models.Model):
    CHECK_TYPES = (

    )
    name = models.CharField(max_length=30)
    api_key = models.CharField(max_length=200)
    check_type = models.CharField()
    point_id = models.IntegerField()


class Check(models.Model):
    printer = models.ForeignKey(Printer, on_delete=models.CASCADE)
    type = models.CharField()
    order = models.JSONField(default=0)
    status = models.CharField(default=0)
    pdf_file = models.FileField(default=0)
