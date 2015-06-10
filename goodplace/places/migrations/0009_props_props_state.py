# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0008_auto_20150610_1716'),
    ]

    operations = [
        migrations.AddField(
            model_name='props',
            name='props_state',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
