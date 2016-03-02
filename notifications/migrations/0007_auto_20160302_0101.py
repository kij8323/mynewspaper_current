# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('comment', '0012_commentdislike_commentlike'),
        ('notifications', '0006_auto_20160302_0019'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='sender_content_type',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='sender_object_id',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='target_content_type',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='target_object_id',
        ),
        migrations.AddField(
            model_name='notification',
            name='sender_object',
            field=models.ForeignKey(default=datetime.datetime(2016, 3, 1, 17, 1, 20, 868638, tzinfo=utc), to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='notification',
            name='target_object',
            field=models.ForeignKey(default=datetime.datetime(2016, 3, 1, 17, 1, 34, 699973, tzinfo=utc), to='comment.Comment'),
            preserve_default=False,
        ),
    ]
