# Generated by Django 3.0.6 on 2020-05-31 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200531_1334'),
    ]

    operations = [
        migrations.AddField(
            model_name='tutorialseries',
            name='series_slug',
            field=models.CharField(default=1, max_length=200),
        ),
    ]
