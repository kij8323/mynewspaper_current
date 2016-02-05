# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20160204_0604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='icon',
            field=models.ImageField(default=b'images/78avatarbig.jpg', null=True, upload_to=b'images', blank=True),
        ),
    ]
