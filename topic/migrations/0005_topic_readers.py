# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0004_auto_20160211_1039'),
    ]

    operations = [
        migrations.AddField(
            model_name='topic',
            name='readers',
            field=models.IntegerField(default=0),
        ),
    ]
