# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-08 21:26
from __future__ import unicode_literals

from django.db import migrations, models
import sitio.models


class Migration(migrations.Migration):

    dependencies = [
        ('sitio', '0008_subastas_titulo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subastas',
            name='imagen1',
        ),
        migrations.AddField(
            model_name='subastas',
            name='imagenA',
            field=models.ImageField(default='', upload_to=sitio.models.upload_to_subastas),
        ),
        migrations.AlterField(
            model_name='subastas',
            name='fechaBaja',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='subastas',
            name='fechaFin',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='subastas',
            name='titulo',
            field=models.CharField(blank=True, max_length=22, null=True),
        ),
    ]
