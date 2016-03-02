# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0007_auto_20160302_0101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='sender_object',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='target_object',
        ),
    ]
