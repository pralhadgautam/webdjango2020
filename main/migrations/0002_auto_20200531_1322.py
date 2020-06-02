# Generated by Django 3.0.6 on 2020-05-31 07:37

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='date published'),
        ),
        migrations.RemoveField(
            model_name='tutorial',
            name='tutorial_series',
        ),
        migrations.AddField(
            model_name='tutorial',
            name='tutorial_series',
            field=models.ManyToManyField(default=1, to='main.TutorialSeries', verbose_name='Series'),
        ),
        migrations.RemoveField(
            model_name='tutorialseries',
            name='tutorial_category',
        ),
        migrations.AddField(
            model_name='tutorialseries',
            name='tutorial_category',
            field=models.ManyToManyField(default=1, to='main.TutorialCategory', verbose_name='Category'),
        ),
    ]
