# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0028_auto_20160427_1005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='cover',
            field=models.BooleanField(default=False, db_index=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='readers',
            field=models.IntegerField(default=0, db_index=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='timestamp',
            field=models.DateTimeField(db_index=True, auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='relation',
            name='timestamp',
            field=models.DateTimeField(db_index=True, auto_now_add=True, null=True),
        ),
    ]
