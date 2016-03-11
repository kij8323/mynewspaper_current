#coding=utf-8
#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.http import Http404
from .models import Group, Topic, TopicForm
from django.contrib import messages
from article.form import CommentForm
from comment.models import Comment
from accounts.models import MyUser
import json
from django.http import HttpResponse
import traceback 
from notifications.signals import notify
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from notifications.atwho import atwho, atwhononoti
# from .forms import TopicForm

# Create your views here.
def group_all(request):
	try:
		group = Group.objects.all()
		# topic = group.topic_set.all()
	except group.DoesNotExist:
		raise Http404("Does not exist")
	paginator = Paginator(group, 5)
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
		# 'group': group,
		'contacts': contacts,
		# 'topic': topic,
		}
	return render(request, 'group_all.html',  context)

def group_index(request):
	topic = Topic.objects.order_by('-updated')

	context = {
		'topic': topic,
		}
	return render(request, 'group_index.html',  context)

def group_detail(request, group_id):
	try:
		group = Group.objects.get(pk=group_id)
		topic = group.topic_set.all()
		context = {
			'group': group,
			'topic': topic,
			}
		print "group_detail"
		print topic
	except group.DoesNotExist:
		raise Http404("Does not exist")
	return render(request, 'group_detail.html',  context)

def topic_detail(request, topic_id):
	try:
		topic = Topic.objects.get(pk=topic_id)
	except topic.DoesNotExist:
		raise Http404("Does not exist")
	comment = Comment.objects.filter(topic=topic).filter(parent=None).order_by('timestamp')
	user = request.user
	paginator = Paginator(comment, 5)
	page = request.GET.get('page')
	try:
		contacts = paginator.page(page)
	except PageNotAnInteger:
	# If page is not an integer, deliver first page.
		contacts = paginator.page(1)
	except EmptyPage:
	# If page is out of range (e.g. 9999), deliver last page of results.
		contacts = paginator.page(paginator.num_pages)
	topic.readers += 1
	topic.save()
	context = {
		'topic':topic,
		'user':user,
		"form": CommentForm,
		"submit_btn": "发表",
		"comment": comment,
		'contacts': contacts,
	}
	return render(request, 'topic_detail.html',  context)

def newtopic(request):
	if request.method == 'POST':
		form = TopicForm(request.POST)
		if form.is_valid():
			content = form.cleaned_data['content']
			title = form.cleaned_data['title']
			new_topic = Topic()
			new_topic.content = content
			new_topic.title = title
			new_topic.writer = request.user
			new_topic.group = Group.objects.get(pk=1)
			new_topic.save()
			return redirect('newtopic')
		else:
			messages.error(request, '您输入的话题内容有误,请改正！')
			return redirect("newtopic")
	else:
		print  request.user
		context = {
			'myform': TopicForm,
			}
	return render(request, 'newtopic.html',  context)

#ajax，发送评论,post
def topicomment(request):
	if request.is_ajax() and request.method == 'POST':
		print request.POST.get('comment')
		text = request.POST.get('comment')
		topicid = request.POST.get('topicid')
		topic = Topic.objects.get(pk=topicid)
		print request.POST.get('comment')
		print request.POST.get('topicid')
		user = request.user
		print user
		try:
			c = Comment(user=user, topic=topic, text=text)
			c.save()
			userlist = atwho(text = text, sender = user, targetcomment = None)
			for item in userlist:
				print 'for item in userlist:'
				atwhouser = MyUser.objects.get(username = item)
				test = "@<a href='" +'/user/'+str(atwhouser.id)+'/informations/'+"'>"+atwhouser.username+"</a>"+' '
				text = text.replace('@'+item+' ', test);
			# c = Comment(user=user, topic=topic, text=text)
			# c.save()
			data = {
			"user": user.username,
			"text": text,
			"commentid": c.id
			}
			print data['commentid']
			json_data = json.dumps(data)
			print 'data'
			return HttpResponse(json_data, content_type='application/json')
		except:
			traceback.print_exc()
			raise Http404(traceback)
	else:
		raise Http404

#ajax，发送评论的评论,post
def topcommentcomment(request):
	if request.is_ajax() and request.method == 'POST':
		text = request.POST.get('comment')
		topicid = request.POST.get('topicid')
		#parenttext = request.POST.get('parenttext')
		preentid = request.POST.get('preentid')
		topic = Topic.objects.get(pk=topicid)
		comment = Comment.objects.filter(topic=topic)
		targetcomment = Comment.objects.get(pk=preentid)
		user = request.user
		print user
		try:
			c = Comment(user=user, topic=topic, text=text, parent=targetcomment)
			c.save()
			userlist = atwho(text = text, sender = user, targetcomment = targetcomment)
			for item in userlist:
				print 'for item in userlist:'
				atwhouser = MyUser.objects.get(username = item)
				test = "@<a href='" +'/user/'+str(atwhouser.id)+'/informations/'+"'>"+atwhouser.username+"</a>"+' '
				text = text.replace('@'+item+' ', test);
			# c = Comment(user=user, topic=topic, text=text, parent=targetcomment)
			# c.save()
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

def atwhoidentify(request):
	if request.is_ajax():
		text = request.POST.get('comment')
		print text
		userlist = atwhononoti(text)
		print 'userlist'
		print userlist
		data = {
			"userlist": userlist,
			}
		json_data = json.dumps(data)
		return HttpResponse(json_data, content_type='application/json')
	else:
		raise Http404