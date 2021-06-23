from django.db import models


class Product (models.Model):
    prod_name = models.CharField(max_length=200)
    prod_type = models.CharField(max_length=200)
    prod_about = models.CharField(max_length=200)
