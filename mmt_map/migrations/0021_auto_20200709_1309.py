# Generated by Django 3.0.6 on 2020-07-09 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mmt_map', '0020_auto_20200709_1309'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='audiofile',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='document',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='image',
            name='tags',
        ),
    ]
