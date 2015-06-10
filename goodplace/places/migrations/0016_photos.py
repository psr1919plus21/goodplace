# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0015_props_props_authorphone'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('props_photourl', models.CharField(default=b'/static/img/photoplace/default.jpg', max_length=200)),
                ('photoprop', models.ForeignKey(to='places.Props')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
