# Generated by Django 2.1.2 on 2018-11-05 21:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cargo', models.PositiveSmallIntegerField(choices=[(1, 'Iniciação Científica'), (2, 'Mestrado'), (3, 'Doutorado'), (4, 'Pós-Doc.')], default=1)),
                ('role', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Aluno'), (2, 'Orientador')], default=1, null=True)),
                ('avatar', models.ImageField(blank=True, upload_to='accounts')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]