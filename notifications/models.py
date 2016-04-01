#coding=utf-8
#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey, GenericRelation
from django.contrib.contenttypes.models import ContentType
from .signals import notify
from ckeditor.fields import RichTextField
from comment.models import Comment
from accounts.models import MyUser
from article.models import Article
from topic.models import Topic
import traceback 
# Create your models here.
class Notification(models.Model):
	#发送消息的对象
	sender_object = models.ForeignKey(MyUser)
	verb = models.CharField(max_length=255)
	#评论内容
	text = RichTextField(max_length=5000, null=True, blank=True)
	target_article = models.ForeignKey(Article, null=True, blank=True)
	target_topic = models.ForeignKey(Topic, null=True, blank=True)
	#目标对象
	target_object = models.ForeignKey(Comment, null=True, blank=True)
	recipient = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='notifications')
	#是否已读
	read = models.BooleanField(default=False)
	#消息发送时间
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)

	def __unicode__(self):
		if self.target_object:
			context = {
				"sender": self.sender_object,
				"verb": self.verb,
				"target": self.target_object.text,
				"text": self.text,
				"recipient": self.recipient
			}
			return "%(sender)s %(verb)s %(recipient)s %(target)s  %(text)s" %context
		else:
			context = {
				"sender": self.sender_object,
				"verb": self.verb,
				"text": self.text,
				"recipient": self.recipient
			}
			return "%(sender)s %(verb)s %(recipient)s  %(text)s" %context


def new_notification(sender, **kwargs):
	print "new_notification"
	kwargs.pop('signal', None)
	target_object = kwargs.pop("target_object", None)
	text = kwargs.pop("text")
	verb = kwargs.pop("verb")
	sender_object = sender
	recipient = kwargs.pop("recipient")
	target_article = kwargs.pop("target_article", None)
	print 'new_notification'
	print target_article
	target_topic = kwargs.pop("target_topic", None)
	print target_topic
	try:
		c = Notification(target_object=target_object, 
						sender_object=sender_object, 
						target_topic=target_topic,
						target_article = target_article,
						recipient=recipient,
						verb = verb,
						text = text,
						)
		c.save()
		print 'success'
	except:
		traceback.print_exc()

notify.connect(new_notification)