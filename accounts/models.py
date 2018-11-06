from django.db import models
from django.contrib.auth.models import User
from . import accoutns_choices as ac
import os



def get_image_path(instance, filename):
    return os.path.join('/home/guibax/PycharmProjects/Fito/accounts/static/accounts/profiles/Guilherme_Niederauer/avatar.jpg', str(instance.id), filename)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(upload_to='accounts', blank=True, )

    def __str__(self):
        return self.user.username



