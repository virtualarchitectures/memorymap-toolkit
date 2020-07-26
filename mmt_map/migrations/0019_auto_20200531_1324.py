# Generated by Django 3.0.6 on 2020-05-31 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mmt_map', '0018_auto_20200531_1244'),
    ]

    operations = [
        migrations.AddField(
            model_name='audiofile',
            name='slug',
            field=models.SlugField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='document',
            name='slug',
            field=models.SlugField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='image',
            name='slug',
            field=models.SlugField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='line',
            name='popup_audio_slug',
            field=models.SlugField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='point',
            name='popup_audio_slug',
            field=models.SlugField(blank=True, max_length=128),
        ),
        migrations.AddField(
            model_name='polygon',
            name='popup_audio_slug',
            field=models.SlugField(blank=True, max_length=128),
        ),
    ]