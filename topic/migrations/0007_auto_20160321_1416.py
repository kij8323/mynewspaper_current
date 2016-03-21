# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('topic', '0006_auto_20160229_0956'),
    ]

    operations = [
        migrations.CreateModel(
            name='Topicreaders',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('readers', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='topic',
            name='readers',
        ),
        migrations.AddField(
            model_name='topicreaders',
            name='topic',
            field=models.ForeignKey(to='topic.Topic'),
        ),
    ]
