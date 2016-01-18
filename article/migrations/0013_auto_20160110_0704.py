# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0012_category_relations'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='writer',
            field=models.ForeignKey(default=datetime.datetime(2016, 1, 10, 7, 4, 31, 426638, tzinfo=utc), to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
