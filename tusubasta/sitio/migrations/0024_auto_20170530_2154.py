# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-30 21:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0023_auto_20170525_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subastas',
            name='fechaFin',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]