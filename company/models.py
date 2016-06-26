#coding=utf-8
#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.db import models
from accounts.models import MyUser
from django.conf import settings
# Create your models here.


class Company(models.Model):
	id = models.AutoField(primary_key=True, db_index=True)
	#公司名称
	title = models.CharField(max_length=120)
	#公司网址
	weburl = models.CharField(max_length=120)
	#公司所在地
	location = models.CharField(max_length=120,null=True)
	#公司所在地
	# address_shi = models.CharField(max_length=120,null=True)
	#主要所属领域
	industry = models.CharField(max_length=120,null=True)
	#一句话简介
	associatetitle = models.CharField(max_length=120,null=True)
	#产品与优势
	product = models.CharField(max_length=2000,null=True)
	#目标用户
	client = models.CharField(max_length=2000,null=True)
	#公司未来
	future = models.CharField(max_length=2000,null=True)
	#相似产品
	sameproduct = models.CharField(max_length=2000,null=True)
	#联系方式
	connection = models.CharField(max_length=120,null=True)
	#公司上传时间
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, null=True, db_index=True)
	# #公司更新时间
	updated = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)
	#团队优势
	team = models.CharField(max_length=2000, null=True, blank=True)
	#公司建立者
	uper = models.ForeignKey(MyUser, db_index=True)
	#计算公司热度
	readers = models.IntegerField(default=0, db_index=True)
	#是否审核通过
	verify = models.BooleanField(default=False, db_index=True)
	#logo
	logo = models.ImageField(upload_to='images/', null=True, blank=True, default='images/companylogo.png')
	#wechat
	wechat = models.ImageField(upload_to='images/', null=True, blank=True)
	def __unicode__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('company_detail', kwargs={"company_id": self.id})

	def get_image_url(self):
		return "%s%s" %(settings.MEDIA_URL, self.logo)




