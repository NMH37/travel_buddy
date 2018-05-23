# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-05-22 21:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='trip',
            name='user',
        ),
        migrations.AddField(
            model_name='trip',
            name='user',
            field=models.ManyToManyField(related_name='trips', to='main.User'),
        ),
    ]
