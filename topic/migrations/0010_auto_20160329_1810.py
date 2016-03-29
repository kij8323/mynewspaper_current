# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0009_auto_20160321_1638'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='updated',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
