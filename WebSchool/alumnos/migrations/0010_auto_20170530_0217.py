# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-30 02:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumnos', '0009_auto_20170530_0215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumnos',
            name='Calificacion',
            field=models.DecimalField(decimal_places=2, max_digits=3),
        ),
    ]
