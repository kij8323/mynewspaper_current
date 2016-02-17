#coding=utf-8
#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import Http404
from .models import Article, Category, Relation
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
	comment = Comment.objects.filter(article=article)
	if len(comment)>5:
		moercomment = True
	else:
		moercomment = False
	comment = comment[:5]
	request.session['lastpage'] = request.get_full_path()
	print 'request.session'
	print request.session['lastpage']
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
	print 'x'