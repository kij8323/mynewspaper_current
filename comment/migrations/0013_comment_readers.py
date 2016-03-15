# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0012_commentdislike_commentlike'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='readers',
            field=models.IntegerField(default=0),
        ),
    ]
