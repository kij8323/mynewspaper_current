# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0013_comment_readers'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='is_privcycomment',
            field=models.BooleanField(default=False),
        ),
    ]
