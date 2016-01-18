#coding=utf-8
#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import Http404
from .models import Article
from .form import CommentForm
from comment.models import Comment
import traceback  
import types  
import json
from django.http import HttpResponse
def article_detail(request, article_id):
	try:
		article = Article.objects.get(pk=article_id)
	except Article.DoesNotExist:
		raise Http404("Article does not exist")
	article.readers += 1
	article.save()
	user = request.user
	comment = Comment.objects.filter(article=article)
	context = {
		'article':article,
		'user':user,
		"form": CommentForm,
		"submit_btn": "发表",
		"comment": comment,
	}
	return render(request, 'article_detail.html',  context)

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
		text = request.POST.get('comment')
		articleid = request.POST.get('articleid')
		parenttext = request.POST.get('parenttext')
		article = Article.objects.get(pk=articleid)
		comment = Comment.objects.filter(article=article)
		print request.POST.get('comment')
		print request.POST.get('articleid')
		user = request.user
		print user
		try:
			c = Comment(user=user, article=article, text=text, parenttext=parenttext)
			c.save()
			data = {
			"user": user.username,
			"text": text,
			"parenttext": parenttext,
			}
			json_data = json.dumps(data)
			return HttpResponse(json_data, content_type='application/json')
		except:
			traceback.print_exc()
			raise Http404(traceback)

	else:
		raise Http404