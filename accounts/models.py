from django.db import models
from django.contrib.auth.models import User
from . import accoutns_choices as choices
import datetime


def user_directory_path(instance, filename):
    users = User.objects.all()
    ins = instance.search()
    print(ins)
    for user in users:
        if user == instance.user:
            if ins == 'avatar':
                return 'accounts/user_{0}/{1}/{2}'.format(instance.user.id, ins, filename)

        elif ins == 'files':
                print("oks")
                return 'accounts/user_{0}/{1}/{2}'.format(instance.user.id, ins, filename)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to=user_directory_path, blank=True, )

    def __str__(self):
        return self.user.username

    def search(self):
        return 'avatar'


class UserProjects(models.Model):
    user = models.ForeignKey(UserProfile, default=None, on_delete=models.CASCADE)
    projeto = models.CharField(max_length=200, default="Projeto")
    data = models.CharField(max_length=11, default="2018")
    nivel = models.PositiveSmallIntegerField(choices=choices.NIVEL_CHOICES)

    def search(self):
        return 'projects'

    def __str__(self):
        return self.user.user.username


class UserUploads(models.Model):
    user = models.ForeignKey(UserProfile, default=None, on_delete=models.CASCADE)
    projetos = models.CharField(max_length=200, default="Projeto")
    docname = models.CharField(max_length=30, null=True, blank=True)
    file = models.FileField(upload_to=user_directory_path)
    type = models.PositiveSmallIntegerField(choices=choices.DOC_TYPES, null=True)


    def search(self):
        return 'files'

    def __str__(self):
        return self.user.user.username


class UserDates(models.Model):
    user = models.ForeignKey(UserProfile, default=None, on_delete=models.CASCADE)
    note_text = models.CharField(max_length=1000)
    note_date = models.DateField(blank=False, null=False)

    def search(self):
        return 'usernotes'

    def __str__(self):
        return self.user.user.username