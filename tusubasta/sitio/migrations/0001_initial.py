# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='cabSubasta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('precioBase', models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)),
                ('fechaAlta', models.DateTimeField(auto_now=True, null=True)),
                ('fechaBaja', models.DateTimeField(auto_now=True, null=True)),
                ('imagen', models.ImageField(upload_to='', blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='calificacion',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('descripcion', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='categoria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('descripcion', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='detSubasta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('valorOferta', models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True)),
                ('fechaOferta', models.DateTimeField(auto_now=True, null=True)),
                ('estado', models.BooleanField(default=True)),
                ('idSubasta', models.ForeignKey(to='sitio.cabSubasta')),
                ('usuarioComprador', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='subCategoria',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('descripcion', models.CharField(blank=True, max_length=50, null=True)),
                ('idCategoria', models.ForeignKey(to='sitio.categoria')),
            ],
        ),
        migrations.AddField(
            model_name='cabsubasta',
            name='idCalificacion',
            field=models.ForeignKey(to='sitio.calificacion'),
        ),
        migrations.AddField(
            model_name='cabsubasta',
            name='idSubcategoria',
            field=models.ForeignKey(to='sitio.subCategoria'),
        ),
        migrations.AddField(
            model_name='cabsubasta',
            name='usuarioVendedor',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL),
        ),
    ]
