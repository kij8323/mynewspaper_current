#coding=utf-8
#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.shortcuts import render
from .models import Company
from django.shortcuts import render, HttpResponseRedirect, redirect
import os
from django.contrib.auth.decorators import login_required  
import json
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.urlresolvers import reverse
# Create your views here.


def company_detail(request, company_id):
	company = Company.objects.get(pk=company_id)
	context = {
		'company' : company,
	}
	return render(request, 'company_detail.html', context)



def company_list(request):
	company = Company.objects.all().order_by('-id')
		# 分页
	paginator = Paginator(company, 7)
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
		'company' : contacts,
	}
	return render(request, 'company_list.html', context)

def company_content_fresh(request):
	if request.session.get('firm-industry', False):
		industry = request.session['firm-industry']
	if request.session.get('firm-financing', False):
		financing = request.session['firm-financing']
	if request.session.get('firm-locationx', False):
		locationx = request.session['firm-locationx']
	if industry == '全部':
		industry = ('智能家居','可穿戴设备', '智能健康','智能配件', '智能母婴设备'
					,'机器人', '无人机','手机平板', 'VR/AR','智能交通', '其它')
		companylist = Company.objects.filter(industry__in=industry)
	else :
		companylist = Company.objects.filter(industry=industry)
	if financing == '全部':
		financing = ('未融资', '种子轮','天使轮', 'Pre-A','A轮', 'B轮'
					,'C轮', 'D轮及以上','其它')			
		companylist = companylist.filter(financing__in=financing)
	else :
		companylist = companylist.filter(financing=financing)
	if locationx == '全部':
		locationx = ('北京市', '上海市','天津市', '重庆市','深圳市', '四川省'
					,'广东省', '其它')	
		companylist = companylist.filter(location__in=locationx)
	else :
		companylist = companylist.filter(location=locationx)		
	print  companylist.count()
	for item in companylist:
		print item.id
		# 分页
	paginator = Paginator(companylist, 7)
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
		"company": contacts,
	}
	return render(request, 'company_content_fresh.html',  context)

def company_list_fresh(request):
	if request.is_ajax():
		request.session['firm-industry'] = str(request.GET.get('industry'))
		request.session['firm-financing'] = str(request.GET.get('financing'))
		request.session['firm-locationx'] = str(request.GET.get('locationx'))
		data = {
			"test": 'ok',
		}
		json_data = json.dumps(data)
		return HttpResponse(json_data, content_type='application/json')
	else:
		raise Http404


@login_required  
def company_built1(request):
	if request.method == 'POST':
		company = Company()
		company.title = request.POST.get('company_title')
		company.weburl = request.POST.get('company_weburl')
		company.uper = request.user
		company.save()
		request.session['company_id'] = company.id
		return redirect('company_built2')
	else:
		return render(request, 'company_built1.html')

@login_required  
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
		if request.method == 'POST':
			if request.POST.get('company_location') == '0':
				company.location = "北京市"
			elif request.POST.get('company_location') == '1':
				company.location = "上海市"
			elif request.POST.get('company_location') == '2':
				company.location = "天津市"
			elif request.POST.get('company_location') == '3':
				company.location = "重庆市"
			elif request.POST.get('company_location') == '4':
				company.location = "深圳市"
			elif request.POST.get('company_location') == '5':
				company.location = "四川省"
			elif request.POST.get('company_location') == '6':
				company.location = "广东省"
			elif request.POST.get('company_location') == '7':
				company.location = "其它"
			if request.POST.get('company_industry') == '0':
				company.industry = "智能家居"
			elif request.POST.get('company_industry') == '1':
				company.industry = "可穿戴设备"
			elif request.POST.get('company_industry') == '2':
				company.industry = "智能健康"
			elif request.POST.get('company_industry') == '3':
				company.industry = "智能配件"
			elif request.POST.get('company_industry') == '4':
				company.industry = "智能母婴设备"
			elif request.POST.get('company_industry') == '5':
				company.industry = "机器人"
			elif request.POST.get('company_industry') == '6':
				company.industry = "无人机"
			elif request.POST.get('company_industry') == '7':
				company.industry = "手机平板"
			elif request.POST.get('company_industry') == '8':
				company.industry = "VR/AR"
			elif request.POST.get('company_industry') == '9':
				company.industry = "智能交通"
			elif request.POST.get('company_industry') == '10':
				company.industry = "其它"
			company.associatetitle = request.POST.get('company_associatetitle')
			company.product = request.POST.get('company_product')
			company.client = request.POST.get('company_client')
			company.financing = '其它'
			company.save()
			return redirect('builtsucss')
		context = {
			'company' : company,
			'company_title' : company.title,
		}
		return render(request, 'company_built2.html', context)
	else:
		return render(request, 'company_built1.html')

@login_required  
def company_built3(request, company_id):
	company = Company.objects.get(pk=company_id)
	action_url = reverse("company_built3", kwargs={"company_id": company_id})
	if request.method == 'POST' and request.FILES.get('img', False):
		image = request.FILES['img']
		company.logo = image
		company.save() 
		os.system('echo yes | python /home/shen/Documents/paperproject/mynewspaper/manage.py collectstatic')
		return redirect(action_url)
	if request.method == 'POST' and request.FILES.get('img1', False):
		image = request.FILES['img1']
		company.images1 = image
		company.save() 
		os.system('echo yes | python /home/shen/Documents/paperproject/mynewspaper/manage.py collectstatic')
		return redirect(action_url)
	if request.method == 'POST' and request.FILES.get('img2', False):
		image = request.FILES['img2']
		company.images2 = image
		company.save() 
		os.system('echo yes | python /home/shen/Documents/paperproject/mynewspaper/manage.py collectstatic')
		return redirect(action_url)
	if request.method == 'POST' and request.FILES.get('img3', False):
		image = request.FILES['img3']
		company.images3 = image
		company.save() 
		os.system('echo yes | python /home/shen/Documents/paperproject/mynewspaper/manage.py collectstatic')
		return redirect(action_url)
	if request.method == 'POST':
		if request.POST.get('company_associatetitle') == '':
			pass
		else:
			company.associatetitle = request.POST.get('company_associatetitle')
		if request.POST.get('company_product') == '':
			pass
		else:
			company.product = request.POST.get('company_product')
		if request.POST.get('company_client') == '':
			pass
		else:
			company.client = request.POST.get('company_client')
		company.sameproduct = request.POST.get('company_sameproduct')
		company.qita = request.POST.get('company_qita')
		company.team = request.POST.get('company_team')
		company.save()
		return redirect('builtsucss')
	context = {
		'company' : company,
	}
	return render(request, 'company_built3.html', context)

def builtsucss(request):
	return render(request, 'builtsucss.html')