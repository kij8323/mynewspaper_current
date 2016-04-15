# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0021_relation_timestamp'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='relation',
            name='timestamp',
        ),
    ]
