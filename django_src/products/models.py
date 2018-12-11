from django.db import models
from django_prometheus.models import ExportModelOperationsMixin


# Create your models here.
class Product(ExportModelOperationsMixin('products'), models.Model):
    CURRENCY_CHOICES = (
        (0, 'us_dollar'),
        (1, 'br_real')
    )
    name = models.CharField(max_length=255)
    price = models.FloatField()
    enterprise_id = models.IntegerField()
    currency = models.CharField(choices=CURRENCY_CHOICES, max_length=1, default=0)
