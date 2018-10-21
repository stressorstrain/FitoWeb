from django.db import models


class Gas(models.Model):
    name = models.CharField(max_length=20)
    cvol = models.IntegerField(default=0)
    porcentage = models.IntegerField(default=0)
    ver_name = models.CharField(default="None", max_length=100)
    ver_date = models.CharField(default="None", max_length=12)

    def __str__(self):
        return self.name
# Create your models here.
