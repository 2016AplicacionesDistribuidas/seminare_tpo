# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-18 01:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escuela', '0005_curso_nombre'),
    ]

    operations = [
        migrations.AddField(
            model_name='curso',
            name='activo',
            field=models.BooleanField(default=True),
        ),
    ]
