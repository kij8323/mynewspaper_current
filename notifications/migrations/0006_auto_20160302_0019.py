# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0005_notification'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='text',
            field=ckeditor.fields.RichTextField(max_length=5000, null=True, blank=True),
        ),
    ]
