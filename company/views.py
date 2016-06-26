#coding=utf-8
#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from .models import Company
from django.shortcuts import render, HttpResponseRedirect, redirect
import os

# Create your views here.


def company_detail(request):
	return 0;



def company_list(request):
	return 0;

def company_built1(request):
	if request.GET.get('company_title', None) and request.GET.get('company_weburl', None):
		company = Company()
		company.title = request.GET.get('company_title')
		company.weburl = request.GET.get('company_weburl')
		company.uper = request.user
		company.save()
		request.session['company_id'] = company.id
		return redirect('company_built2')
	else:
		return render(request, 'company_built1.html')

def company_built2(request):
	if request.session.get('company_id', False):
		company_id = request.session['company_id']
		company = Company.objects.get(pk=company_id)
		if request.method == 'POST' and request.FILES.get('img', False):
			image = request.FILES['img']
			company.logo = image
			company.save() 
			os.system('echo yes | python /home/shen/Documents/paperproject/mynewspaper/manage.py collectstatic')
			return redirect('company_built2')
		if request.GET.get('company_location', None) and request.GET.get('company_industry', None):
			print request.GET.get('company_location')
			if request.GET.get('company_location') == '0':
				print 'x'
				company.location = "北京市"
			elif request.GET.get('company_location') == '1':
				company.location = "上海市"
			elif request.GET.get('company_location') == '2':
				company.location = "天津市"
			elif request.GET.get('company_location') == '3':
				company.location = "重庆市"
			elif request.GET.get('company_location') == '4':
				company.location = "深圳市"
			elif request.GET.get('company_location') == '5':
				company.location = "其它"
			elif request.GET.get('company_location') == '6':
				company.location = "四川省"
			elif request.GET.get('company_industry') == '7':
				company.location = "广东省"
			if request.GET.get('company_industry') == '0':
				company.industry = "电子商务"
			elif request.GET.get('company_industry') == '1':
				company.industry = "社交网络"
			elif request.GET.get('company_industry') == '2':
				company.industry = "智能硬件"
			elif request.GET.get('company_industry') == '3':
				company.industry = "媒体门户"
			elif request.GET.get('company_industry') == '4':
				company.industry = "工具软件"
			elif request.GET.get('company_industry') == '5':
				company.industry = "消费生活"
			elif request.GET.get('company_industry') == '6':
				company.industry = "金融"
			elif request.GET.get('company_industry') == '7':
				company.industry = "医疗健康"
			elif request.GET.get('company_industry') == '8':
				company.industry = "企业服务"
			elif request.GET.get('company_industry') == '9':
				company.industry = "旅游户外"
			elif request.GET.get('company_industry') == '10':
				company.industry = "房产家居"
			elif request.GET.get('company_industry') == '11':
				company.industry = "数字娱乐"
			elif request.GET.get('company_industry') == '12':
				company.industry = "在线教育"
			elif request.GET.get('company_industry') == '13':
				company.industry = "汽车交通"
			elif request.GET.get('company_industry') == '14':
				company.industry = "其它"
			elif request.GET.get('company_industry') == '15':
				company.industry = "物流"
			company.save()
			context = {
				'company' : company,
				'company_title' : company.title,
			}
			return render(request, 'company_built2.html', context)
		context = {
			'company' : company,
			'company_title' : company.title,
		}
		return render(request, 'company_built2.html', context)
	else:
		return render(request, 'company_built1.html')