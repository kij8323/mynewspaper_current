# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='content',
            field=ckeditor.fields.RichTextField(max_length=5000, null=True, blank=True),
        ),
    ]
