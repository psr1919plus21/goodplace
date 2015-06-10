# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0007_auto_20150610_1715'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='props',
            name='props_price',
        ),
        migrations.RemoveField(
            model_name='props',
            name='props_state',
        ),
    ]
