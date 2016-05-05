# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0027_auto_20160427_1000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collection',
            name='id',
            field=models.AutoField(db_index=True, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='relation',
            name='id',
            field=models.AutoField(db_index=True, serialize=False, primary_key=True),
        ),
    ]
