#coding=utf-8
#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from article.models import Article, Category
from topic.models import Group, Topic
from comment.models import Comment
import datetime
from datetime import timedelta
import json
from django.http import HttpResponse
from sphinxapi import *
import sys
from django.core.cache import cache
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def index_search(request):
	q = request.GET.get('search_word')
	if q:
		mode = SPH_MATCH_ALL
		host = 'localhost'
		port = 9312
		index = '*'
		filtercol = 'group_id'
		filtervals = []
		sortby = ''
		groupby = ''
		groupsort = '@group desc'
		limit = 0
		cl = SphinxClient()
		cl.SetServer ( host, port )
		cl.SetWeights ( [100, 1] )
		cl.SetMatchMode ( mode )
		res = cl.Query ( q, index )
		if not res:
			print 'query failed: %s' % cl.GetLastError()
			sys.exit(1)
		if cl.GetLastWarning():
			print 'WARNING: %s\n' % cl.GetLastWarning()
		index = [] #查询结果的id集合
		if res.has_key('matches'):
			for match in res['matches']:
				index.append(match['id'])  
		test = Article.objects.all().filter(id__in = index).order_by('-timestamp') #获得属于id集合的对象的queryset
		print (test.count())
		cache.set("search_word", q)
		# 分页
		paginator = Paginator(test, 10)
		page = request.GET.get('page')
		try:
			contacts = paginator.page(page)
		except PageNotAnInteger:
		# If page is not an integer, deliver first page.
			contacts = paginator.page(1)
		except EmptyPage:
		# If page is out of range (e.g. 9999), deliver last page of results.
			contacts = paginator.page(paginator.num_pages)
		context = {
			'articlequery' : contacts,
			'search_word' : q,
		}
	else:
		context = {
			'articlequery' : None,
		}
	return render(request, 'index_search.html', context)

def home(request):
	coverarticle = Article.objects.all().filter(timestamp__gte=datetime.date.today() - timedelta(days=30)).filter(cover = True).order_by("-timestamp")[0:3]
	covertopic = Topic.objects.all().filter(timestamp__gte=datetime.date.today() - timedelta(days=30)).filter(cover = True).order_by("-timestamp")[0:1]
	print covertopic.count()
	queryset = Article.objects.all().order_by('-timestamp')[0:15]
	topic = Topic.objects.all().filter(timestamp__gte=datetime.date.today() - timedelta(days=30)).order_by("-readers")[0:5]
	#一个月内，最热文章排序
	hotnews = Article.objects.all().filter(timestamp__gte=datetime.date.today() - timedelta(days=30)).order_by("-readers")[0:5]
	nicecomment = Comment.objects.all().filter(timestamp__gte=datetime.date.today() - timedelta(days=30)).order_by("-readers")[0:5]
	context = {
	'queryset': queryset,
	'topicquery' : topic,
	'hotnews': hotnews,
	'nicecomment': nicecomment,
	'coverarticle': coverarticle,
	'covertopic': covertopic[0],
	}
	return render(request, 'home.html', context)
	#return render(request, 'home.html')

def aboutus(request):
	return render(request, 'aboutus.html')

def contactus(request):
	return render(request, 'contactus.html')

def morearticlehome(request):
	if request.is_ajax():
		request.session['homearticlelen'] = request.POST.get('homearticlelen')
		homearticlelen = int(request.session['homearticlelen'])
		article = Article.objects.all().order_by('-timestamp')
		print request.session['homearticlelen']
	if article.count() == homearticlelen:
		loadcompleted = '已全部加载完成'
	else:
		loadcompleted = '点击加载更多'
		print request.session['homearticlelen']
	print loadcompleted
	data = {
		"loadcompleted": loadcompleted,
	}
	json_data = json.dumps(data)
	return HttpResponse(json_data, content_type='application/json')

def articlepagehome(request):
	if request.session.get('homearticlelen', False):
		homearticlelen = request.session['homearticlelen']
	homearticle = Article.objects.all().order_by('-timestamp')
	homearticlelen = int(homearticlelen)
	print homearticlelen
	articlequery = homearticle[homearticlelen:homearticlelen+5]
	context = {
		"articlequery": articlequery,
	}
	return render(request, 'articlepagehome.html',  context)