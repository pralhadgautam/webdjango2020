# Generated by Django 3.0.6 on 2020-05-31 11:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_tutorialseries_series_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutorialseries',
            name='series_slug',
        ),
    ]
