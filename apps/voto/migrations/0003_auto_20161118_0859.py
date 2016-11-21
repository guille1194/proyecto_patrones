# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voto', '0002_auto_20161117_0832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pregunta',
            name='propietario',
            field=models.ForeignKey(related_name='usuarion', blank=True, to='voto.usuario', null=True),
        ),
    ]
