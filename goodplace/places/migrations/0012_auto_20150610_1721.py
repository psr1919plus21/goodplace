# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0011_props_props_postfix'),
    ]

    operations = [
        migrations.AlterField(
            model_name='props',
            name='props_postfix',
            field=models.CharField(default=b'mes', max_length=200),
            preserve_default=True,
        ),
    ]
