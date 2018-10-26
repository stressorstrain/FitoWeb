# Generated by Django 2.1.2 on 2018-10-26 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gas_control', '0005_remove_gas_mvol'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gas',
            old_name='cvol',
            new_name='ars',
        ),
        migrations.RemoveField(
            model_name='gas',
            name='name',
        ),
        migrations.AddField(
            model_name='gas',
            name='ars_p',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='gas',
            name='h2',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='gas',
            name='h2_p',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='gas',
            name='he_p',
            field=models.IntegerField(default=0),
        ),
    ]
