# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-10 21:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('escuela', '0009_alumno_activo'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumno',
            name='egreso',
            field=models.BooleanField(default=False),
        ),
    ]
