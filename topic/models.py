#coding=utf-8
from django.db import models
from accounts.models import MyUser
# Create your models here.
class Group(models.Model):
	#文章名称
	title = models.CharField(max_length=120)
	#文章上传时间
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
	#文章更新时间
	updated = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)
	#作者
	founder = models.ForeignKey(MyUser)
	#文章地址
	url_address = models.CharField(max_length=500, null=True, blank=True)
	#文章图标
	image = models.ImageField(upload_to='images/', null=True, blank=True)
	#自定义查询语句
	#objects = ArticleManager()
	def __unicode__(self):
		return self.title

	def get_image_url(self):
		return "%s%s" %(settings.STATIC_URL, self.image)

	def blockid(self):
		blockid = "block"+str(self.id)
		return blockid

	def get_absolute_url(self):
		return reverse('group_detail', kwargs={"group_id": self.id})

class Topic(models.Model):
	#文章名称
	title = models.CharField(max_length=120)
	#文章上传时间
	timestamp = models.DateTimeField(auto_now_add=True, auto_now=False, null=True)
	#文章更新时间
	updated = models.DateTimeField(auto_now_add=False, auto_now=True, null=True)
	#作者
	writer = models.ForeignKey(MyUser)
	#文章内容
	content = models.TextField(max_length=5000, null=True, blank=True)
	#文章地址
	url_address = models.CharField(max_length=500, null=True, blank=True)
	#文章图标
	image = models.ImageField(upload_to='images/', null=True, blank=True)
	group = models.ForeignKey(Group)
	#自定义查询语句
	#objects = ArticleManager()
	def __unicode__(self):
		return self.title

	def get_image_url(self):
		return "%s%s" %(settings.STATIC_URL, self.image)

	def blockid(self):
		blockid = "block"+str(self.id)
		return blockid

	def get_absolute_url(self):
		return reverse('topic_detail', kwargs={"topic_id": self.id})