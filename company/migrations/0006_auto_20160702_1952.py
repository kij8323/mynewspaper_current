# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0005_company_financing'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='qita',
            field=models.CharField(max_length=2000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='connection',
            field=models.CharField(max_length=120, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='financing',
            field=models.CharField(max_length=120, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='future',
            field=models.CharField(max_length=2000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='sameproduct',
            field=models.CharField(max_length=2000, null=True, blank=True),
        ),
    ]
