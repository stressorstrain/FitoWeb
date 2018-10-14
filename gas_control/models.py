from django.db import models


class Gas(models.Model):
    name = models.CharField(max_length=251)
    mvol = models.IntegerField(default=0)
    cvol = models.IntegerField(default=0)
    porcentage = models.IntegerField(default=0)

    def __str__(self):
        return self.name
# Create your models here.
