# Generated by Django 2.1.2 on 2018-10-17 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gas_control', '0003_auto_20181017_0846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gas',
            name='ver_date',
            field=models.CharField(default='None', max_length=12),
        ),
    ]