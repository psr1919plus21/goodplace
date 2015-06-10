# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_props'),
    ]

    operations = [
        migrations.AddField(
            model_name='props',
            name='props_city',
            field=models.CharField(default=b'city', max_length=200),
            preserve_default=True,
        ),
    ]
