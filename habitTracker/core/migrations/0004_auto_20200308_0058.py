# Generated by Django 3.0.4 on 2020-03-08 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20200307_1830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='value_entry',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
