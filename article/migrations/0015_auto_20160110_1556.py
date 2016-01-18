# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('article', '0014_auto_20160110_1537'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=120)),
                ('associatetitle', models.CharField(max_length=120)),
                ('timestamp', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('content', models.TextField(max_length=5000, null=True, blank=True)),
                ('fromner', models.TextField(max_length=500, null=True, blank=True)),
                ('url_address', models.CharField(max_length=500, null=True, blank=True)),
                ('image', models.ImageField(null=True, upload_to=b'images/', blank=True)),
                ('writer', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
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
        migrations.AddField(
            model_name='category',
            name='relations',
            field=models.ManyToManyField(to='article.Article', through='article.Relation'),
        ),
    ]
