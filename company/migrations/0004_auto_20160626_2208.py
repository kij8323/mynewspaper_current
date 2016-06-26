# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0003_auto_20160625_1920'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='address_sheng',
        ),
        migrations.RemoveField(
            model_name='company',
            name='address_shi',
        ),
        migrations.RemoveField(
            model_name='company',
            name='mainindustry',
        ),
        migrations.RemoveField(
            model_name='company',
            name='subindustry1',
        ),
        migrations.RemoveField(
            model_name='company',
            name='subindustry2',
        ),
        migrations.RemoveField(
            model_name='company',
            name='subindustry3',
        ),
        migrations.AddField(
            model_name='company',
            name='industry',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='location',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
