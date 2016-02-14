# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor_uploader.fields


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0002_auto_20160205_0704'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='content',
            field=ckeditor_uploader.fields.RichTextUploadingField(max_length=5000, null=True, blank=True),
        ),
    ]
