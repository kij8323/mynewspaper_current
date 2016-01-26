# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0003_remove_notification_recipient'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='sender_content_type',
        ),
        migrations.RemoveField(
            model_name='notification',
            name='target_content_type',
        ),
        migrations.DeleteModel(
            name='Notification',
        ),
    ]
