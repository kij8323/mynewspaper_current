# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0012_topic_cover'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collectiontopic',
            name='id',
            field=models.AutoField(db_index=True, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='group',
            name='id',
            field=models.AutoField(db_index=True, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='topic',
            name='id',
            field=models.AutoField(db_index=True, serialize=False, primary_key=True),
        ),
    ]
