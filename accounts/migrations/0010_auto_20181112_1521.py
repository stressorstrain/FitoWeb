# Generated by Django 2.1.2 on 2018-11-12 17:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_userdates'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdates',
            name='note_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
