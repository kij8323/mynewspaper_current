#coding=utf-8
#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from .form import LoginForm, RegisterForm
from .models import MyUser
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import json
from django.http import HttpResponse
from captcha.models import CaptchaStore
from captcha.helpers import captcha_image_url

#登录页面
def loggin(request):
	form = LoginForm(request.POST or None)
	next_url = request.GET.get('next')
	action_url = reverse("loggin")
	print "ajxax"
	if form.is_valid():
		human = True
		print 'human = True'
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		print username, password
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			if next_url is not None:
				return HttpResponseRedirect(next_url)
			return redirect("home")
		else:
			messages.error(request, '用户名与密码不匹配，请重新输入！')
	context = {
		"form": form,
		"action_url": action_url,
		"submit_btn": "登录",
		}
	return render(request, 'loggin.html',  context)


#注册页面
def register(request):
	form = RegisterForm(request.POST or None)
	action_url = reverse("register")
	if form.is_valid():
		human = True
		username = form.cleaned_data['username']
		email = form.cleaned_data['email']
		password = form.cleaned_data['password2']
		new_user = MyUser()
		new_user.username = username
		new_user.email = email
		new_user.set_password(password) #RIGHT
		new_user.save()
		print username, password
		#return render(request,'base_1.html')
		return redirect(reverse('home'))
	context = {
		"form": form,
		"action_url": action_url,
		"submit_btn": "注册",
		}
	return render(request, 'register.html',  context)
	#return redirect("home")

def logout_view(request):
    logout(request)
    return redirect(reverse('home'))

#ajax，验证码刷新
def captchaview(request):
	print 'ajaxxxxxxxxxxxxxxxxxxxxxxx'
	if request.is_ajax():
		captchakey = CaptchaStore.generate_key()
		acptchaimg = captcha_image_url(captchakey)
		data = {
			"captchakey": captchakey,
			"acptchaimg": acptchaimg,
		}
		json_data = json.dumps(data)
		return HttpResponse(json_data, content_type='application/json')
	else:
		raise Http404


#ajax，验证用户名是否已被注册,post
def accountsview(request):
	if request.is_ajax() and request.method == 'POST':
		print 'accountsview'
		print request.POST.get('username')
		username = request.POST.get('username')
        try:
			exists = MyUser.objects.get(username=username)
			data = {
				"message": '该用户名已被注册',
			}
			json_data = json.dumps(data)
			request.session['user_message'] = '该用户名已被注册'
			request.session['user_message_color'] = 'errorlist'
			print request.session['user_message']
			return HttpResponse(json_data, content_type='application/json')
        except MyUser.DoesNotExist:
			data = {
				"message": '恭喜，该用户名可注册！',
			}
			json_data = json.dumps(data)
			request.session['user_message'] = '恭喜，该用户名可注册！'
			request.session['user_message_color'] = 'successlist'
			print request.session['user_message']
			return HttpResponse(json_data, content_type='application/json')
	else:
		raise Http404

#ajax，验证用户名是否已被注册,get
def usernamemessage(request):	
	if request.is_ajax():
		print 'get'
		user_message = request.session['user_message']
		classname = request.session['user_message_color']
		data = {
			"message": user_message,
			"classname": classname,
		}
		json_data = json.dumps(data)
		print 'post'
		return HttpResponse(json_data, content_type='application/json')
	else:
		raise Http404


def userdashboard(request, user_id):	
	try:
		user = MyUser.objects.get(pk=user_id)
	except MyUser.DoesNotExist:
		raise Http404("MyUser does not exist")
	return render(request, 'user_detail.html',  {'user': user})

def userdashboard_comment(request):	
	print 'userdashboard_comment(request)'
	if request.is_ajax():
		print 'userdashboard_comment(request)'
		data = {
			"test": 'test',
		}
		json_data = json.dumps(data)
		return HttpResponse(json_data, content_type='application/json')
	else:
		raise Http404