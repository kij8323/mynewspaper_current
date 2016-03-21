# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0007_auto_20160321_1416'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topicreaders',
            name='topic',
        ),
        migrations.AddField(
            model_name='topic',
            name='readers',
            field=models.IntegerField(default=0),
        ),
        migrations.DeleteModel(
            name='Topicreaders',
        ),
    ]
