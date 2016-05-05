# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0014_comment_is_privcycomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='id',
            field=models.AutoField(db_index=True, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='commentdislike',
            name='id',
            field=models.AutoField(db_index=True, serialize=False, primary_key=True),
        ),
        migrations.AlterField(
            model_name='commentlike',
            name='id',
            field=models.AutoField(db_index=True, serialize=False, primary_key=True),
        ),
    ]
