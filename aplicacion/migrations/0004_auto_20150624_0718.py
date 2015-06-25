# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0003_auto_20150624_0712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicacion',
            name='usuario',
            field=models.ForeignKey(to='aplicacion.Usuario'),
        ),
    ]
