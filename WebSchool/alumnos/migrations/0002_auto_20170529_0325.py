# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-29 03:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumnos',
            name='Contra',
            field=models.CharField(default='wuisho', max_length=16),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='alumnos',
            name='Curso',
            field=models.CharField(blank=True, default='programacion', max_length=200),
        ),
    ]