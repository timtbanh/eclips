# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-26 21:52
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('when', models.DateTimeField(default=datetime.datetime.now)),
                ('address', models.CharField(max_length=200)),
                ('isPerformed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Barber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('phone', models.IntegerField()),
                ('address', models.CharField(max_length=200, null=True)),
                ('price', models.TextField(max_length=200, null=True)),
                ('walkin', models.CharField(max_length=200, null=True)),
                ('description', models.TextField(null=True)),
                ('avgRating', models.IntegerField(null=True)),
                ('profilePic', models.CharField(max_length=200, null=True)),
                ('schedule', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('phone', models.IntegerField()),
                ('address', models.CharField(max_length=200, null=True)),
                ('description', models.TextField(null=True)),
                ('avgRating', models.IntegerField(null=True)),
                ('profilePic', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('rating', models.IntegerField()),
                ('appointment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.Appointment')),
            ],
        ),
        migrations.AddField(
            model_name='appointment',
            name='barber',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Barber'),
        ),
        migrations.AddField(
            model_name='appointment',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Client'),
        ),
    ]
