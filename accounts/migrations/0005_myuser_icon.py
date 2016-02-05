# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20160110_0704'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='icon',
            field=models.ImageField(null=True, upload_to=b'images/', blank=True),
        ),
    ]
