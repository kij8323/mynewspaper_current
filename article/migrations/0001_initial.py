# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=120)),
                ('timestamp', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('content', models.TextField(max_length=5000, null=True, blank=True)),
                ('writer', models.TextField(max_length=500, null=True, blank=True)),
                ('fromner', models.TextField(max_length=500, null=True, blank=True)),
                ('url_address', models.CharField(max_length=500, null=True, blank=True)),
                ('image', models.ImageField(null=True, upload_to=b'static/images/', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField(max_length=5000, null=True, blank=True)),
                ('introduction', models.TextField(max_length=5000, null=True, blank=True)),
                ('image', models.ImageField(null=True, upload_to=b'static/images/', blank=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Relation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('article', models.ForeignKey(to='article.Article')),
                ('category', models.ForeignKey(to='article.Category')),
            ],
        ),
    ]
