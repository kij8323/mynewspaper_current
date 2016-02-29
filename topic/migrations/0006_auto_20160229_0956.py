# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0005_topic_readers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='group',
            old_name='url_address',
            new_name='associatetitle',
        ),
    ]
