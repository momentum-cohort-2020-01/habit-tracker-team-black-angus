# Generated by Django 3.0.4 on 2020-03-08 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20200308_0059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='log',
            name='habit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='habits', to='core.Habit'),
        ),
    ]