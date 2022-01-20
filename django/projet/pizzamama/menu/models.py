from django.db import models
from django.test import ignore_warnings

# Create your models here.

class Pizza(models.Model):
    nom = models.CharField(max_length=200)
    ingredients = models.CharField(max_length=400)
    prix = models.FloatField(default=0)
    vegan = models.BooleanField(default=False)