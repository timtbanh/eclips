# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-07 22:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='appointment',
            old_name='isPerformed',
            new_name='isCompleted',
        ),
        migrations.AlterField(
            model_name='barber',
            name='phone',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='client',
            name='phone',
            field=models.CharField(max_length=200),
        ),
    ]