# Generated by Django 2.1.2 on 2018-11-10 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_auto_20181109_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useruploads',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(1, '.docx'), (2, '.xlsx'), (3, '.ppx')]),
        ),
    ]
