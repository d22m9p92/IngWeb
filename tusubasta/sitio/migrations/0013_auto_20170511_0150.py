# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-11 01:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0012_auto_20170509_0003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subastas',
            name='titulo',
            field=models.CharField(max_length=22, null=True),
        ),
    ]