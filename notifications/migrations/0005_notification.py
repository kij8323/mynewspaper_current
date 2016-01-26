# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('notifications', '0004_auto_20160126_1349'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sender_object_id', models.PositiveIntegerField()),
                ('verb', models.CharField(max_length=255)),
                ('text', models.TextField()),
                ('target_object_id', models.PositiveIntegerField(null=True, blank=True)),
                ('read', models.BooleanField(default=False)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('recipient', models.ForeignKey(related_name='notifications', to=settings.AUTH_USER_MODEL)),
                ('sender_content_type', models.ForeignKey(related_name='nofity_sender', to='contenttypes.ContentType')),
                ('target_content_type', models.ForeignKey(related_name='notify_target', blank=True, to='contenttypes.ContentType', null=True)),
            ],
        ),
    ]
