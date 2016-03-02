# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0011_auto_20160302_0132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='target_object',
            field=models.ForeignKey(blank=True, to='comment.Comment', null=True),
        ),
    ]
