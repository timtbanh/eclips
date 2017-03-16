# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-16 19:53
from __future__ import unicode_literals

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20170316_1244'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='client',
            name='height_field',
        ),
        migrations.RemoveField(
            model_name='client',
            name='width_field',
        ),
        migrations.AlterField(
            model_name='client',
            name='profilePic',
            field=models.ImageField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='/media/clients'), upload_to=b''),
        ),
    ]
