# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0005_auto_20151229_1639'),
    ]

    operations = [
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
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='content',
            field=models.TextField(max_length=5000, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='article',
            name='fromner',
            field=models.TextField(max_length=500, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(null=True, upload_to=b'static/images/', blank=True),
        ),
        migrations.AddField(
            model_name='article',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
        migrations.AddField(
            model_name='article',
            name='url_address',
            field=models.CharField(max_length=500, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='article',
            name='writer',
            field=models.TextField(max_length=500, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='relation',
            name='article',
            field=models.ForeignKey(to='article.Article'),
        ),
        migrations.AddField(
            model_name='relation',
            name='category',
            field=models.ForeignKey(to='article.Category'),
        ),
    ]
