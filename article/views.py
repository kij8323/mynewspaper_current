#coding=utf-8
#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import Http404
from .models import Article, Category, Relation, Collection
from .form import CommentForm
from comment.models import Comment
import traceback  
import types  
import json
from django.http import HttpResponse
from notifications.signals import notify
from accounts.models import MyUser


def article_detail(request, article_id):
	try:
		article = Article.objects.get(pk=article_id)
		numofcomment = article.comment_set.count()
		numwriter = article.writer.article_set.count()
		category = Category.objects.all()
		numreaders = 0
		for x in article.writer.article_set.all():
			numreaders = x.readers + numreaders
		print numreaders
		print 'numwriter'
		print numwriter
	except Article.DoesNotExist:
		raise Http404("Article does not exist")
	article.readers += 1
	hotarticle = Article.objects.order_by('-readers')[:5]
	article.save()
	user = request.user
	collection = Collection.objects.filter(article=article, user=user.id)
	print type(collection)
	if collection: 
		collection = '已收藏'
	else:
		collection = '收藏'
	comment = Comment.objects.filter(article=article)
	if comment.count() > 5:
		moercomment = True
	else:
		moercomment = False
	comment = comment[:5]
	request.session['lastpage'] = request.get_full_path()
	thisrelationtag = Relation.objects.filter(article=article)
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
			notify.send(sender=user, target_object=targetcomment, verb="@", text=text)
			print 'z'
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
	print comment.count()
	print request.session['commentlen']
	print 'morecomment'
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


def test(request):
	context = {
		'x': 'x',
	}
	return render(request, 'test.html',  context)