# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='address',
        ),
        migrations.AddField(
            model_name='company',
            name='address_sheng',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='company',
            name='address_shi',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='associatetitle',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='client',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='connection',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='future',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='mainindustry',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='product',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='sameproduct',
            field=models.CharField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='subindustry1',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='subindustry2',
            field=models.CharField(max_length=120, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='subindustry3',
            field=models.CharField(max_length=120, null=True),
        ),
    ]
