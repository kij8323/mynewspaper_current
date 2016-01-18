# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0011_article_associatetitle'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='relations',
            field=models.ManyToManyField(to='article.Article', through='article.Relation'),
        ),
    ]
