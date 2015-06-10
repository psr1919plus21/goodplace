# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0010_props_props_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='props',
            name='props_postfix',
            field=models.CharField(default=b'dcd', max_length=200),
            preserve_default=True,
        ),
    ]
