# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_props_props_city'),
    ]

    operations = [
        migrations.AddField(
            model_name='props',
            name='props_home',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='props',
            name='props_street',
            field=models.CharField(default=b'city', max_length=200),
            preserve_default=True,
        ),
    ]
