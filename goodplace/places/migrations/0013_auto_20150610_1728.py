# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0012_auto_20150610_1721'),
    ]

    operations = [
        migrations.AddField(
            model_name='props',
            name='props_authorlastname',
            field=models.CharField(default=b'ivanov', max_length=20),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='props',
            name='props_authorname',
            field=models.CharField(default=b'ivan', max_length=20),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='props',
            name='props_authorpatronymic',
            field=models.CharField(default=b'ivanovich', max_length=20),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='props',
            name='props_furniture',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='props',
            name='props_howater',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='props',
            name='props_internet',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='props',
            name='props_kids',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='props',
            name='props_linens',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='props',
            name='props_microwave',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='props',
            name='props_pets',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='props',
            name='props_utensils',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='props',
            name='props_washmachine',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='props',
            name='props_postfix',
            field=models.CharField(default=b'mes', max_length=20),
            preserve_default=True,
        ),
    ]
