from django.db import models


class Gas(models.Model):
    #name = models.CharField(max_length=20)
    #cvol = models.IntegerField(default=0)
    ars = models.IntegerField(default=0)
    ars_p = models.IntegerField(default=0)
    h2 = models.IntegerField(default=0)
    h2_p = models.IntegerField(default=0)
    he = models.IntegerField(default=0)
    he_p = models.IntegerField(default=0)
    porcentage = models.IntegerField(default=0)
    ver_name = models.CharField(default="None", max_length=100)
    ver_date = models.CharField(default="None", max_length=12)

   # def __str__(self):
       # return self.name
# Create your models here.


class Usuarios(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

