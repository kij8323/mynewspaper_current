#coding=utf-8
#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from django.conf import settings
from accounts.models import MyUser
from django.core.urlresolvers import reverse
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.db.models.signals import post_save
from django.dispatch import receiver
import os
from django.core.cache import cache

# Create your models here.
class Article(models.Model):
	#文章名称
	title = models.CharField(max_length=120)
	associatetitle = models.CharField(max_length=120)
	#文章上传时间
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
	#timestamp = models.DateTimeField('date published')
	# #文章更新时间
	updated = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)
	#文章内容
	content = RichTextUploadingField(max_length=5000, null=True, blank=True)
	#作者
	writer = models.ForeignKey(MyUser)
	#转载
	fromner = models.TextField(max_length=500, null=True, blank=True)
	#文章地址
	url_address = models.CharField(max_length=500, null=True, blank=True)
	#文章图标
	image = models.ImageField(upload_to='images/', null=True, blank=True)
	#文章图标是否显示在文章内容中
	images_show = models.BooleanField(default=False)
	#是否为封面
	cover = models.BooleanField(default=False)
	#自定义查询语句
	#objects = ArticleManager()
	#collections = models.ManyToManyField(MyUser, through='Collection', through_fields=('user', 'article'),related_name='ArticleCollection')

	readers = models.IntegerField(default=0)
	# shares = models.IntegerField(default=0)
	# collections = models.IntegerField(default=0)

	def __unicode__(self):
		return self.title

	def get_image_url(self):
		return "%s%s" %(settings.MEDIA_URL, self.image)

	def blockid(self):
		blockid = "block"+str(self.id)
		return blockid

	def get_absolute_url(self):
		return reverse('article_detail', kwargs={"article_id": self.id})

class Category(models.Model):
	#类别名称
	title = models.CharField(max_length=120)
	#类别描述
	description = models.TextField(max_length=5000, null=True, blank=True)
	introduction = models.TextField(max_length=5000, null=True, blank=True)
	#类别图标
	image = models.ImageField(upload_to='images/', null=True, blank=True)
	#image_detail = models.ImageField(upload_to='static/images/', null=True, blank=True)
	#类别生成时间
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
	#类别更新时间
	updated = models.DateTimeField(auto_now_add=False, auto_now=True)
	#自定义查询
	#objects = CategoryManager()
	relations = models.ManyToManyField(Article, through='Relation', )

	def __unicode__(self):
		return self.title
		
	def get_image_url(self):
		return "%s%s" %(settings.MEDIA_URL, self.image)

	def get_absolute_url(self):
		return reverse('category_detail', kwargs={"category_id": self.id})

class Relation(models.Model):
	category = models.ForeignKey(Category)
	article = models.ForeignKey(Article)
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)

class Collection(models.Model):
	user = models.ForeignKey(MyUser)
	article = models.ForeignKey(Article)

#每个文章实例生成，都会自动添加分类和重新建立引索
@receiver(post_save, sender=Article)
def categoryofarticle(sender, **kwargs):
    article = kwargs.pop("instance")
    thisrelationtag = Relation.objects.filter(article=article)
    if thisrelationtag:
    	return;
    else:
		category = Category.objects.get(id = 3)
		relation = Relation(article= article, category = category)
		relation.save()
		# cachekey = "article_readers_" + str(article.id)
		# cache.set(cachekey, 0)
		# cache.incr(cachekey)
		# print cache.get(cachekey)

