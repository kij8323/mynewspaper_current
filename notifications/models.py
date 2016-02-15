#coding=utf-8
#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from .signals import notify

# Create your models here.
class Notification(models.Model):
	#发送消息的对象
	sender_content_type = models.ForeignKey(ContentType, related_name='nofity_sender')
	sender_object_id = models.PositiveIntegerField()
	sender_object = GenericForeignKey("sender_content_type", "sender_object_id")
	verb = models.CharField(max_length=255)
	#评论内容
	text = models.TextField()
	#目标对象
	target_content_type = models.ForeignKey(ContentType, related_name='notify_target', 
		null=True, blank=True)
	target_object_id = models.PositiveIntegerField(null=True, blank=True)
	target_object = GenericForeignKey("target_content_type", "target_object_id")
	recipient = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='notifications')
	#是否已读
	read = models.BooleanField(default=False)
	#消息发送时间
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

	def __unicode__(self):
		context = {
			"sender": self.sender_object,
			"verb": self.verb,
			"target": self.target_object.text,
			"text": self.text,
			"recipient": self.recipient
		}
		return "%(sender)s %(verb)s %(target)s %(recipient)s %(text)s" %context


def new_notification(sender, **kwargs):
	print "new_notification"
	kwargs.pop('signal', None)
	target_object = kwargs.pop("target_object")
	text = kwargs.pop("text")
	verb = kwargs.pop("verb")
	sender_object = sender
	recipient = target_object.user
	try:
		c = Notification(target_object=target_object, 
						sender_object=sender_object, 
						recipient=recipient,
						verb = verb,
						text = text,
						)
		c.save()
	except:
		traceback.print_exc()

notify.connect(new_notification)