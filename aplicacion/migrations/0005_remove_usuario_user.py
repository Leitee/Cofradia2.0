# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aplicacion', '0004_auto_20150624_0718'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='user',
        ),
    ]
