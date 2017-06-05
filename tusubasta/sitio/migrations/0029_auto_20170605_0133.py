# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-05 01:33
from __future__ import unicode_literals

from django.db import migrations, models
import sitio.models


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0028_auto_20170603_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subastas',
            name='imagenA',
            field=models.ImageField(blank=True, default='', null=True, upload_to=sitio.models.upload_to_subastas),
        ),
        migrations.AlterField(
            model_name='subastas',
            name='imagenB',
            field=models.ImageField(blank=True, default='', null=True, upload_to=sitio.models.upload_to_subastas),
        ),
        migrations.AlterField(
            model_name='subastas',
            name='imagenC',
            field=models.ImageField(blank=True, default='', null=True, upload_to=sitio.models.upload_to_subastas),
        ),
    ]
