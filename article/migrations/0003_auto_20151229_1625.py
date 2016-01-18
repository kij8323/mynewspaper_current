# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_auto_20151229_1617'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='content',
        ),
        migrations.RemoveField(
            model_name='article',
            name='fromner',
        ),
        migrations.RemoveField(
            model_name='article',
            name='image',
        ),
        migrations.RemoveField(
            model_name='article',
            name='timestamp',
        ),
        migrations.RemoveField(
            model_name='article',
            name='updated',
        ),
        migrations.RemoveField(
            model_name='article',
            name='url_address',
        ),
        migrations.RemoveField(
            model_name='article',
            name='writer',
        ),
    ]
