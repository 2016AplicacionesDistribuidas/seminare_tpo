# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-07-22 13:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('escuela', '0022_auto_20170720_2217'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='curso',
            unique_together=set([('nombre', 'plan')]),
        ),
    ]