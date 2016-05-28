# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0017_auto_20160528_1058'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='read',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='notification',
            name='recipient',
            field=models.ForeignKey(related_name='notifications', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='notification',
            name='sender_object',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
