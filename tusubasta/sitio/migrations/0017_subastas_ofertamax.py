# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-20 18:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0016_auto_20170517_0134'),
    ]

    operations = [
        migrations.AddField(
            model_name='subastas',
            name='ofertaMax',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=7, null=True),
        ),
    ]