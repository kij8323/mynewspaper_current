# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0007_auto_20160703_2210'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='images1',
            field=models.ImageField(default=b'images/companylogo.png', null=True, upload_to=b'images/', blank=True),
        ),
        migrations.AddField(
            model_name='company',
            name='images2',
            field=models.ImageField(default=b'images/companylogo.png', null=True, upload_to=b'images/', blank=True),
        ),
        migrations.AddField(
            model_name='company',
            name='images3',
            field=models.ImageField(default=b'images/companylogo.png', null=True, upload_to=b'images/', blank=True),
        ),
    ]
