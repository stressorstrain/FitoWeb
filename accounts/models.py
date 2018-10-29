from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
import os
# Create your models here.


def get_image_path(instance, filename):
    return os.path.join('/home/guibax/PycharmProjects/Fito/accounts/static/accounts/profiles/Guilherme_Niederauer/avatar.jpg', str(instance.id), filename)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    form = models.CharField(max_length=50, default='Estudante')
    profile_image = models.ImageField(upload_to =get_image_path, blank=True, null=True)

    def __str__(self):
        return self.user.username


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])


post_save.connect(create_profile, sender=User)
