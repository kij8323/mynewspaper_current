# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0024_relation_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='images_show',
            field=models.BooleanField(default=False),
        ),
    ]
