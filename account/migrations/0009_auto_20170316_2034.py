# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-17 03:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_auto_20170316_1911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barber',
            name='profilePic',
            field=models.ImageField(null=True, upload_to='clients'),
        ),
        migrations.AlterField(
            model_name='client',
            name='profilePic',
            field=models.ImageField(null=True, upload_to=b''),
        ),
    ]
