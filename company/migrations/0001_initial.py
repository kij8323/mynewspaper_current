# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(db_index=True, serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=120)),
                ('weburl', models.CharField(max_length=120)),
                ('address', models.CharField(max_length=120)),
                ('mainindustry', models.CharField(max_length=120)),
                ('subindustry1', models.CharField(max_length=120)),
                ('subindustry2', models.CharField(max_length=120)),
                ('subindustry3', models.CharField(max_length=120)),
                ('associatetitle', models.CharField(max_length=120)),
                ('product', models.CharField(max_length=2000)),
                ('client', models.CharField(max_length=2000)),
                ('future', models.CharField(max_length=2000)),
                ('sameproduct', models.CharField(max_length=2000)),
                ('connection', models.CharField(max_length=120)),
                ('timestamp', models.DateTimeField(db_index=True, auto_now_add=True, null=True)),
                ('updated', models.DateTimeField(auto_now=True, null=True)),
                ('team', models.CharField(max_length=2000, null=True, blank=True)),
                ('readers', models.IntegerField(default=0, db_index=True)),
                ('verify', models.BooleanField(default=False, db_index=True)),
                ('logo', models.ImageField(null=True, upload_to=b'images/', blank=True)),
                ('wechat', models.ImageField(null=True, upload_to=b'images/', blank=True)),
                ('uper', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
