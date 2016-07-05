# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_auto_20160626_2208'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='financing',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
