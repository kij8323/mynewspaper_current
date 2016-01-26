# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notifications', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='recipient',
            field=models.ForeignKey(related_name='notifications', default=datetime.datetime(2016, 1, 25, 9, 3, 31, 55941, tzinfo=utc), to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
