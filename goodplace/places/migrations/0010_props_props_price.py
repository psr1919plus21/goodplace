# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0009_props_props_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='props',
            name='props_price',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
