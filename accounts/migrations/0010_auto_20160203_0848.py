# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20160203_0823'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='icon',
            field=models.FileField(null=True, upload_to=b'images', blank=True),
        ),
    ]
