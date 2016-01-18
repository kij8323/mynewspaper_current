# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0013_auto_20160110_0704'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='writer',
        ),
        migrations.RemoveField(
            model_name='category',
            name='relations',
        ),
        migrations.RemoveField(
            model_name='relation',
            name='article',
        ),
        migrations.RemoveField(
            model_name='relation',
            name='category',
        ),
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Relation',
        ),
    ]
