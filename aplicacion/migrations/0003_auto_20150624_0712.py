# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('aplicacion', '0002_auto_20150624_0242'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='user',
            field=models.ForeignKey(default=datetime.datetime(2015, 6, 24, 7, 12, 38, 412804, tzinfo=utc), to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='publicacion',
            name='usuario',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
