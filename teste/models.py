from django.db import models

# Create your models here.
class People(models.Model):
    cnpj = models.CharField(max_lenght=14)
    name = models.CharField(max_lenght=200)
    