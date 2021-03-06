from django.db import models
from django.db import models
from django import forms



class Product(models.Model):
    GTIN = models.BigIntegerField(unique=True)
    name = models.CharField(max_length=25)
    price = models.FloatField(max_length=25)
    expiryDate = models.DateTimeField(max_length=25)

