from django.db import models

# Create your models here.
class Dj(models.Model):
    start = models.CharField(max_length=100)
    end = models.CharField(max_length=100)
    cities = models.CharField(max_length=200)
