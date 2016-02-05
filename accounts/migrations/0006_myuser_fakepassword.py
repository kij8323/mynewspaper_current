# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_myuser_icon'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='fakepassword',
            field=models.CharField(max_length=255, null=True, blank=True),
        ),
    ]
