# Generated by Django 3.0.6 on 2020-07-15 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mmt_map', '0024_auto_20200710_0828'),
    ]

    operations = [
        migrations.AddField(
            model_name='line',
            name='published',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='point',
            name='published',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='polygon',
            name='published',
            field=models.BooleanField(default=True),
        ),
    ]
