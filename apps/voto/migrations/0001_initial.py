# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('ID_Categoria', models.AutoField(serialize=False, primary_key=True)),
                ('num_cat', models.IntegerField(unique=True)),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Eleccion',
            fields=[
                ('ID_Eleccion', models.AutoField(serialize=False, primary_key=True)),
                ('eleccion', models.CharField(max_length=1, choices=[(b'SI', b'Si'), (b'NO', b'No')])),
            ],
        ),
        migrations.CreateModel(
            name='Encuesta',
            fields=[
                ('ID_Encuesta', models.AutoField(serialize=False, primary_key=True)),
                ('titulo', models.CharField(max_length=64)),
                ('categoria', models.CharField(max_length=64)),
                ('fecha_creacion', models.DateField(default=datetime.date.today)),
                ('publicado', models.BooleanField(default=True)),
            ],
            options={
                'ordering': ['-fecha_creacion'],
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('ID_Usuario', models.AutoField(serialize=False, primary_key=True)),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=64)),
                ('last', models.CharField(max_length=64)),
                ('user_perfil', models.OneToOneField(related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Voto',
            fields=[
                ('ID_Voto', models.AutoField(serialize=False, primary_key=True)),
                ('eleccion', models.ForeignKey(to='voto.Eleccion')),
                ('encuesta', models.ForeignKey(to='voto.Encuesta')),
                ('usuario', models.ForeignKey(to='voto.Usuario')),
            ],
        ),
        migrations.AddField(
            model_name='encuesta',
            name='propietario',
            field=models.ForeignKey(related_name='usuarion', blank=True, to='voto.Usuario', null=True),
        ),
        migrations.AddField(
            model_name='eleccion',
            name='encuesta',
            field=models.ForeignKey(to='voto.Encuesta'),
        ),
        migrations.AlterUniqueTogether(
            name='voto',
            unique_together=set([('usuario', 'encuesta')]),
        ),
    ]
