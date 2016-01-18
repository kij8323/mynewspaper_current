# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0002_auto_20160112_1610'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-timestamp']},
        ),
        migrations.AddField(
            model_name='comment',
            name='parenttext',
            field=models.TextField(default=datetime.datetime(2016, 1, 17, 14, 4, 44, 463327, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
