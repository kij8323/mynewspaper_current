# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0010_auto_20151229_1730'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='associatetitle',
            field=models.CharField(default=datetime.datetime(2015, 12, 31, 7, 44, 53, 825060, tzinfo=utc), max_length=120),
            preserve_default=False,
        ),
    ]
