# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import ckeditor.fields
from django.utils.timezone import utc
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('comment', '0012_commentdislike_commentlike'),
        ('notifications', '0009_auto_20160302_0127'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='read',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='notification',
            name='recipient',
            field=models.ForeignKey(related_name='notifications', to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='notification',
            name='sender_object',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='notification',
            name='target_object',
            field=models.ForeignKey(to='comment.Comment', null=True),
        ),
        migrations.AddField(
            model_name='notification',
            name='text',
            field=ckeditor.fields.RichTextField(max_length=5000, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='notification',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 1, 17, 31, 17, 933271, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='notification',
            name='verb',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
