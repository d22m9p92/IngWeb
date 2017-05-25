# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-25 21:29
from __future__ import unicode_literals

from django.db import migrations, models
import sitio.models


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0022_auto_20170521_1957'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='likes',
            name='idSubasta',
        ),
        migrations.RemoveField(
            model_name='likes',
            name='idUsuarioVendedor',
        ),
        migrations.AlterField(
            model_name='subastas',
            name='imagenA',
            field=models.ImageField(default='', null=True, upload_to=sitio.models.upload_to_subastas),
        ),
        migrations.AlterField(
            model_name='subastas',
            name='imagenB',
            field=models.ImageField(default='', null=True, upload_to=sitio.models.upload_to_subastas),
        ),
        migrations.AlterField(
            model_name='subastas',
            name='imagenC',
            field=models.ImageField(default='', null=True, upload_to=sitio.models.upload_to_subastas),
        ),
        migrations.DeleteModel(
            name='Likes',
        ),
    ]
