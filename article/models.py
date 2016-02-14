#coding=utf-8
from django.db import models
from django.conf import settings
from accounts.models import MyUser
from django.core.urlresolvers import reverse
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
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
	#自定义查询语句
	#objects = ArticleManager()

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
	relations = models.ManyToManyField(Article, through='Relation')

	def __unicode__(self):
		return self.title
		
	def get_image_url(self):
		return "%s%s%s" %(settings.STATIC_URL, settings.MEDIA_URL, self.image)


class Relation(models.Model):
	category = models.ForeignKey(Category)
	article = models.ForeignKey(Article)