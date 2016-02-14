# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import ckeditor_uploader.fields
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0003_auto_20160211_0656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(default=datetime.datetime(2016, 2, 11, 10, 39, 43, 853216, tzinfo=utc), max_length=5000),
            preserve_default=False,
        ),
    ]
