# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0009_auto_20160211_0911'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(default=datetime.datetime(2016, 2, 11, 10, 6, 58, 649855, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
