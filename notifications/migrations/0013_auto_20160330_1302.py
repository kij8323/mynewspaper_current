# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0020_collection'),
        ('topic', '0010_auto_20160329_1810'),
        ('notifications', '0012_auto_20160302_1243'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='target_article',
            field=models.ForeignKey(blank=True, to='article.Article', null=True),
        ),
        migrations.AddField(
            model_name='notification',
            name='target_topic',
            field=models.ForeignKey(blank=True, to='topic.Topic', null=True),
        ),
    ]
