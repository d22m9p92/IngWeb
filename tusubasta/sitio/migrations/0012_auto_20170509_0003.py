# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-09 00:03
from __future__ import unicode_literals

from django.db import migrations, models
import sitio.models


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0011_auto_20170508_2253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subastas',
            name='imagenA',
            field=models.ImageField(blank=True, default='', null=True, upload_to=sitio.models.upload_to_subastas),
        ),
    ]
