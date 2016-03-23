#coding=utf-8
#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import Http404
from .models import Article, Category, Relation, Collection
from .form import CommentForm
from comment.models import Comment, CommentLike, CommentDisLike
import traceback  
import types  
import json
from django.http import HttpResponse
from notifications.signals import notify
from accounts.models import MyUser
from notifications.atwho import atwho
from itertools import chain

# def 

def article_detail(request, article_id):
	try:
		article = Article.objects.get(pk=article_id)
		#文章回复数
		numofcomment = article.comment_set.count()
		#作者文章总数
		numwriter = article.writer.article_set.count()
		#文章所有类别
		category = Category.objects.all()
		#作者所有文章总阅读数
		numreaders = 0
		for x in article.writer.article_set.all():
			numreaders = x.readers + numreaders
		print numreaders
		print 'numwriter'
		print numwriter
	except Article.DoesNotExist:
		raise Http404("Article does not exist")
	#阅读数+1
	article.readers += 1
	#最热文章排序
	hotarticle = Article.objects.order_by('-readers')[:5]
	article.save()
	#当前读者对象
	user = request.user
	#读者是否收藏该文章
	collection = Collection.objects.filter(article=article, user=user.id)
	print type(collection)
	if collection: 
		collection = '已收藏'
	else:
		collection = '收藏'
	#文章回复按热度排序
	commentorderbyreaders = Comment.objects.filter(article=article).filter(readers__gt=3).order_by('-readers')[0:3]
	commentorderbyreaderscount = commentorderbyreaders.count()
	#文章回复按时间
	comment = Comment.objects.filter(article=article).order_by('-timestamp')
	#文章回复数大于5才有更多回复按钮
	if comment.count() > 5:
		moercomment = True
	else:
		moercomment = False#链接最热回复和按时间排序的回复
	#链接热度排序和时间排序回复
	# comment = list(chain(commentorderbyreaders, comment))
	# comment = sorted(set(comment), key=comment.index) 
	#显示头5个回复
	comment = comment[:5]
	#把本页地址装入session
	request.session['lastpage'] = request.get_full_path()
	#print request.path﻿﻿
	sharelink = request.get_host()+request.get_full_path()
	print sharelink
	#文章属于哪些类别
	thisrelationtag = Relation.objects.filter(article=article)
	print thisrelationtag[0].category
	#同属与一类的其他文章
	thisrelationtagarticle = Relation.objects.filter(category=thisrelationtag[0].category).exclude(article = article)
	if thisrelationtagarticle.count()==0:
		thisrelationtagarticle = Relation.objects.filter(category=thisrelationtag[1].category).exclude(article = article)
	if thisrelationtagarticle.count()==0:
		thisrelationtagarticle = Relation.objects.filter(category=thisrelationtag[2].category).exclude(article = article)
	#文章被多少人收藏过
	usercollectioncount = Collection.objects.filter(article=article).count()
	context = {
		'article':article,
		'user':user,
		"form": CommentForm,
		"submit_btn": "发表",
		"comment": comment,
		'numofcomment': numofcomment,
		'numwriter': numwriter,
		'numreaders': numreaders,
		'hotarticle': hotarticle,
		'category': category,
		'moercomment': moercomment,
		'collection' : collection,
		'thisrelationtag' : thisrelationtag,
		'thisrelationtagarticle': thisrelationtagarticle[0:3], 
		'usercollectioncount' : usercollectioncount, 
		'sharelink': sharelink,
		"commentorderbyreaders": commentorderbyreaders,
	}
	return render(request, 'article_detail.html',  context)




def category_detail(request, category_id):
	try:
		category = Category.objects.get(pk=category_id)
		x = Relation.objects.filter(category=category)
	except Category.DoesNotExist:
		raise Http404("Category does not exist")
	context = {
		'x': x,
	}
	return render(request, 'category_detail.html',  context)


#ajax，发送评论,post
def articlecomment(request):
	if request.is_ajax() and request.method == 'POST':
		print request.POST.get('comment')
		text = request.POST.get('comment')
		articleid = request.POST.get('articleid')
		article = Article.objects.get(pk=articleid)
		print request.POST.get('comment')
		print request.POST.get('articleid')
		user = request.user
		print user
		try:
			c = Comment(user=user, article=article, text=text)
			c.save()
			userlist = atwho(text = text, sender = user, targetcomment = None)
			for item in userlist:
				print 'for item in userlist:'
				atwhouser = MyUser.objects.get(username = item)
				test = "@<a href='" +'/user/'+str(atwhouser.id)+'/informations/'+"'>"+atwhouser.username+"</a>"+' '
				text = text.replace('@'+item+' ', test);
			# c = Comment(user=user, article=article, text=text)
			# c.save()
			data = {
			"user": user.username,
			"text": text,
			"commentid": c.id
			}
			json_data = json.dumps(data)
			return HttpResponse(json_data, content_type='application/json')
		except:
			traceback.print_exc()
			raise Http404(traceback)
	else:
		raise Http404

#ajax，发送评论的评论,post
def commentcomment(request):
	if request.is_ajax() and request.method == 'POST':
		print 'commentcomment'
		text = request.POST.get('comment')
		articleid = request.POST.get('articleid')
		#parenttext = request.POST.get('parenttext')
		preentid = request.POST.get('preentid')
		article = Article.objects.get(pk=articleid)
		comment = Comment.objects.filter(article=article)
		targetcomment = Comment.objects.get(pk=preentid)
		print 'commentcomment'
		print 'x'
		print 'y'
		print 'z'
		user = request.user
		print user
		try:
			c = Comment(user=user, article=article, text=text, parent=targetcomment)
			c.save()
			targetcomment.readers = targetcomment.readers + 1
			targetcomment.save()
			userlist = atwho(text = text, sender = user, targetcomment = targetcomment)
			print 'z'
			for item in userlist:
				print 'for item in userlist:'
				atwhouser = MyUser.objects.get(username = item)
				test = "@<a href='" +'/user/'+str(atwhouser.id)+'/informations/'+"'>"+atwhouser.username+"</a>"+' '
				text = text.replace('@'+item+' ', test);
			# c = Comment(user=user, article=article, text=text, parent=targetcomment)
			# c.save()
			data = {
			"user": user.username,
			"text": text,
			"parentcommentext": c.parent.text,
			"parentcommentuser": str(c.parent.user),
			"commentid":c.id,
			}
			json_data = json.dumps(data)
			return HttpResponse(json_data, content_type='application/json')
		except:
			traceback.print_exc()
			raise Http404(traceback)

	else:
		raise Http404


def morecomment(request):
	try:
		articleid = request.POST.get('articleid')
		article = Article.objects.get(pk=articleid)
		comment = Comment.objects.filter(article=article)
		print 'morecomment'
	except Article.DoesNotExist:
		raise Http404("Article does not exist")
	if request.is_ajax():
		request.session['commentlen'] = request.POST.get('commentlen')
	if comment.count() == int(request.session['commentlen']):
		loadcompleted = '已全部加载完成'
	else:
		loadcompleted = '点击加载更多'
	data = {
		'loadcompleted' : loadcompleted
	}
	json_data = json.dumps(data)
	return HttpResponse(json_data, content_type='application/json')

def collection(request):
	print 'collection'
	try:
		articleid = request.POST.get('articleid')
		article = Article.objects.get(pk=articleid)
		user = request.user
	except Article.DoesNotExist:
		raise Http404("Article does not exist")
	collection = Collection.objects.filter(article=article, user=user)
	print type(collection)
	if collection: 
		collection.delete()
		collecicon = '收藏'
	else:
		c = Collection(user=user, article=article)
		c.save()
		collecicon = '已收藏'
	data = {
	 'collecicon': collecicon,
	}
	json_data = json.dumps(data)
	return HttpResponse(json_data, content_type='application/json')

def commentlike(request):
	try:
		commentid = request.POST.get('commentid')
		comment = Comment.objects.get(pk=commentid)
		user = request.user
		print 'commentlikecommentlike'
	except Article.DoesNotExist:
		raise Http404("Article does not exist")
	commentlike = CommentLike.objects.filter(comment=comment, user=user)
	print 'commentlike'
	if commentlike: 
		commentlike.delete()
		comment.readers = comment.readers - 1
		comment.save()
	else:
		comment.readers = comment.readers + 1
		comment.save()
		c = CommentLike(user=user, comment=comment)
		c.save()
	commentlikecount = CommentLike.objects.filter(comment=comment).count()
	print 'commentlike'
	print commentlikecount
	data = {
	 'commentlikecount': commentlikecount,
	}
	json_data = json.dumps(data)
	print 'commentlike'
	return HttpResponse(json_data, content_type='application/json')

def commentdislike(request):
	try:
		commentid = request.POST.get('commentid')
		comment = Comment.objects.get(pk=commentid)
		user = request.user
		print 'commentlike'
	except Article.DoesNotExist:
		raise Http404("Article does not exist")
	commentdislike = CommentDisLike.objects.filter(comment=comment, user=user)
	print 'commentlike'
	if commentdislike: 
		commentdislike.delete()
		comment.readers = comment.readers - 1
		comment.save()
	else:
		comment.readers = comment.readers + 1
		comment.save()
		c = CommentDisLike(user=user, comment=comment)
		c.save()
	commentdislikecount = CommentDisLike.objects.filter(comment=comment).count()
	print commentdislikecount
	data = {
	 'commentdislikecount': commentdislikecount,
	}
	json_data = json.dumps(data)
	print 'commentlike'
	return HttpResponse(json_data, content_type='application/json')

def commentpage(request, article_id):
	try:
		article = Article.objects.get(pk=article_id)
		comment = Comment.objects.filter(article=article)
	except Article.DoesNotExist:
		raise Http404("Article does not exist")
	print 'test'
	if request.session.get('commentlen', False):
		commentlen = request.session['commentlen']
	print 'test'
	print commentlen
	commentlen = int(commentlen)
	comment = comment[commentlen:commentlen+5]
	context = {
		"comment": comment,
	}
	return render(request, 'commentpage.html',  context)



from topic.models import Group, Topic, TopicForm
def test(request):
	context = {
		'x': 'x',
		'myform': TopicForm,
	}
	return render(request, 'test.html',  context)
