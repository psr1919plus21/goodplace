# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0006_props_props_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='props',
            name='props_price',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='props',
            name='props_state',
            field=models.BooleanField(),
            preserve_default=True,
        ),
    ]
