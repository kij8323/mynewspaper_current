# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0008_auto_20160321_1458'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='topicount',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='topic',
            name='updated',
            field=models.DateTimeField(null=True),
        ),
    ]
