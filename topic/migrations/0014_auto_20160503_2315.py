# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0013_auto_20160427_1005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='timestamp',
            field=models.DateTimeField(db_index=True, auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='topic',
            name='cover',
            field=models.BooleanField(default=False, db_index=True),
        ),
    ]
