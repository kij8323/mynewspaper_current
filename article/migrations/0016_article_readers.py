# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0015_auto_20160110_1556'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='readers',
            field=models.IntegerField(default=0),
        ),
    ]
