# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-18 22:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0014_auto_20170318_1531'),
    ]

    operations = [
        migrations.AddField(
            model_name='barber',
            name='avgRating',
            field=models.FloatField(null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='avgRating',
            field=models.FloatField(null=True),
        ),
    ]