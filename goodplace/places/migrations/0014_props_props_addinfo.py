# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0013_auto_20150610_1728'),
    ]

    operations = [
        migrations.AddField(
            model_name='props',
            name='props_addinfo',
            field=models.TextField(default=b'text'),
            preserve_default=True,
        ),
    ]
