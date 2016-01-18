# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_article_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2015, 12, 29, 16, 39, 59, 318979, tzinfo=utc), verbose_name=b'date published'),
            preserve_default=False,
        ),
    ]
