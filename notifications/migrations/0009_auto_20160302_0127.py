# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0008_auto_20160302_0117'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='read',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='recipient',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='text',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='timestamp',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='verb',
        ),
    ]
