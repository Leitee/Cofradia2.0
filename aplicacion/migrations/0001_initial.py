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
            name='Calificacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('calificacion', models.IntegerField()),
                ('tipo', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Postulante',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='Publicacion',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=100)),
                ('fechaInicio', models.DateField()),
                ('fechaCierre', models.DateField()),
                ('cantidad', models.IntegerField()),
                ('descripcion', models.CharField(max_length=300)),
                ('categoria', models.ForeignKey(to='aplicacion.Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fechaNacimiento', models.DateField()),
                ('sexo', models.CharField(max_length=10)),
                ('telefono', models.CharField(max_length=20)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='publicacion',
            name='usuario',
            field=models.ForeignKey(to='aplicacion.Usuario'),
        ),
        migrations.AddField(
            model_name='postulante',
            name='publicacion',
            field=models.ForeignKey(to='aplicacion.Publicacion'),
        ),
        migrations.AddField(
            model_name='postulante',
            name='usuario',
            field=models.ForeignKey(to='aplicacion.Usuario'),
        ),
        migrations.AddField(
            model_name='calificacion',
            name='publicacion',
            field=models.ForeignKey(to='aplicacion.Publicacion'),
        ),
        migrations.AddField(
            model_name='calificacion',
            name='usuario',
            field=models.ForeignKey(to='aplicacion.Usuario'),
        ),
    ]
