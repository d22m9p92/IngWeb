# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-31 00:32
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0004_perfil_moderador'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil',
            name='moderador',
        ),
    ]
