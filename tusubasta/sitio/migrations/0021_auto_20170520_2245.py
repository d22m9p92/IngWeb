# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-20 22:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sitio', '0020_auto_20170520_2216'),
    ]

    operations = [
        migrations.CreateModel(
            name='Denuncias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fechaDenuncia', models.DateTimeField(blank=True, default=None, null=True)),
                ('idComentario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sitio.Comentarios')),
                ('idRespuesta', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='sitio.Respuestas')),
                ('idUsuario', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AlterField(
            model_name='likes',
            name='fechaAlta',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
        migrations.AlterField(
            model_name='likes',
            name='fechaBaja',
            field=models.DateTimeField(blank=True, default=None, null=True),
        ),
    ]