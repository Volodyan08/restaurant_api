import uuid
from django.db import models


class Printer(models.Model):
    PRINTER_TYPE = (
        ("K", "KITCHEN"),
        ("C", "CLIENT"),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=30)
    api_key = models.CharField(max_length=200)
    check_type = models.CharField(choices=PRINTER_TYPE, max_length=32)
    point_id = models.IntegerField()


class Check(models.Model):
    CHECK_TYPE = (
        ("K", "KITCHEN"),
        ("C", "CLIENT"),
    )
    CHECK_STATUS = (
        ("N", "NEW"),
        ("R", "RENDERED"),
        ("P", "PRINTED"),
    )
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    printer = models.ForeignKey(Printer, on_delete=models.CASCADE)
    type = models.CharField(choices=CHECK_TYPE, max_length=32)
    order = models.JSONField()
    status = models.CharField(default="N", choices=CHECK_STATUS, max_length=32)
    pdf_file = models.FileField(default=0)
