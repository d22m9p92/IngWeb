# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-08 22:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0010_auto_20170508_2251'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subastas',
            old_name='imagen1',
            new_name='imagenA',
        ),
        migrations.RenameField(
            model_name='subastas',
            old_name='imagen2',
            new_name='imagenB',
        ),
        migrations.RenameField(
            model_name='subastas',
            old_name='imagen3',
            new_name='imagenC',
        ),
    ]
