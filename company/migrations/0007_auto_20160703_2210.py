# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0006_auto_20160702_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='client',
            field=ckeditor.fields.RichTextField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='future',
            field=ckeditor.fields.RichTextField(max_length=2000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='product',
            field=ckeditor.fields.RichTextField(max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='qita',
            field=ckeditor.fields.RichTextField(max_length=2000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='sameproduct',
            field=ckeditor.fields.RichTextField(max_length=2000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='company',
            name='team',
            field=ckeditor.fields.RichTextField(max_length=2000, null=True, blank=True),
        ),
    ]
