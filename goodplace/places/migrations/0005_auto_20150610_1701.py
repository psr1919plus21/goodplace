# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_auto_20150610_1657'),
    ]

    operations = [
        migrations.AddField(
            model_name='props',
            name='props_place',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='props',
            name='props_rating',
            field=models.FloatField(default=0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='props',
            name='props_sleepplace',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='props',
            name='props_street',
            field=models.CharField(default=b'street', max_length=200),
            preserve_default=True,
        ),
    ]
