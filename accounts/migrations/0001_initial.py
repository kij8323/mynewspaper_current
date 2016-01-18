# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0011_article_associatetitle'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(null=True, verbose_name='last login', blank=True)),
                ('username', models.CharField(unique=True, max_length=255)),
                ('email', models.EmailField(max_length=255, verbose_name=b'email address')),
                ('timestamp', models.DateTimeField(auto_now_add=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserConecction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('article', models.ForeignKey(to='article.Article')),
                ('user', models.ForeignKey(to='accounts.MyUser')),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(null=True, upload_to=b'images/', blank=True)),
                ('company_name', models.CharField(max_length=50, null=True, blank=True)),
                ('profession', models.CharField(max_length=20, null=True, blank=True)),
                ('qq_address', models.CharField(max_length=20, null=True, blank=True)),
                ('weixin_address', models.CharField(max_length=20, null=True, blank=True)),
                ('my_introduction', models.CharField(max_length=30, null=True, blank=True)),
                ('user', models.OneToOneField(to='accounts.MyUser')),
            ],
        ),
    ]
