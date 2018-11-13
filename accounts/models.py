from django.db import models
from django.contrib.auth.models import User
from . import accoutns_choices as choices
import datetime


def user_directory_path(instance, filename):
    users = User.objects.all()
    ins = instance.search()
    for user in users:
        if ins == 'avatar':
            if user == instance.user:
                return 'accounts/user_{0}/{1}/{2}'.format(instance.user.id, ins, filename)

        else:
            if user.username == instance.username:
                ins = instance.search()
                return 'accounts/user_{0}/{1}/{2}'.format(user.id, ins, filename)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    avatar = models.ImageField(upload_to=user_directory_path, blank=True, )

    def __str__(self):
        return self.user.username

    def search(self):
        print("UserProfile")
        return 'avatar'


class UserProjects(models.Model):
    username = models.CharField(max_length=200, default="Projeto")
    projeto = models.CharField(max_length=200, default="Projeto")
    data = models.CharField(max_length=11, default="2018")


class UserUploads(models.Model):
    username = models.CharField(max_length=200, default="Docs")
    docname = models.CharField(max_length=30, null=True, blank=True)
    file = models.FileField(upload_to=user_directory_path)
    type = models.PositiveSmallIntegerField(choices=choices.DOC_TYPES, null=True)

    def search(self):
        print("UserUploads")
        return 'docs'


class UserDates(models.Model):
    username = models.CharField(max_length=200)
    note_text = models.CharField(max_length=1000)
    note_date = models.DateField(blank=False, null=False)

    def search(self):
        return 'usernotes'
