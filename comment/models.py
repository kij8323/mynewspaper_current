#coding=utf-8
from django.db import models
from accounts.models import MyUser
from article.models import Article
from topic.models import Topic
from ckeditor.fields import RichTextField
from django.forms import ModelForm
# Create your models here.
class Comment(models.Model):
	#发表评论用户
	user = models.ForeignKey(MyUser)
	#评论的父评论
	parent = models.ForeignKey("self", null=True, blank=True)
	#评论的视频
	article = models.ForeignKey(Article, null=True, blank=True)
	topic = models.ForeignKey(Topic, null=True, blank=True)
	#评论内容
	text = RichTextField(max_length=5000, null=True, blank=True)
	#评论发表时间
	updated = models.DateTimeField(auto_now=True, auto_now_add=False)
	#评论修改时间
	timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
	#自定义查询
	# objects = CommentManager()
	#回复的评论用户
	reponse = models.CharField(max_length=255, null=True, blank=True)
	
	parenttext = models.TextField(null=True, blank=True)

	class Meta:
		ordering = ['-timestamp']

	def __unicode__(self):
		return self.user.username

	def is_child(self):
		if self.parent is not None:
			return True
		else:
			return False



#text = RichTextField(max_length=5000, null=True, blank=True)

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']