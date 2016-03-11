#coding=utf-8
#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django import template
register = template.Library()
import re, sys
from notifications.signals import notify
from accounts.models import MyUser
reload(sys)
sys.setdefaultencoding( "utf-8" )


@register.filter
def time_chinese_week(value): 
    return value.replace('week', u'星期');

@register.filter
def time_chinese_weeks(value): 
    return value.replace('weeks', u'星期');

@register.filter
def time_chinese_minus(value): 
    return value.replace('minutes', u'分钟');

@register.filter
def time_chinese_minu(value): 
    return value.replace('minute', u'分钟');

@register.filter
def time_chinese_day(value): 
    return value.replace('day', u'天');

@register.filter
def time_chinese_days(value): 
    return value.replace('days', u'天');

@register.filter
def time_chinese_hour(value): 
    return value.replace('hour', u'小时');

@register.filter
def time_chinese_hours(value): 
    return value.replace('hours', u'小时');

@register.filter
def comma(value): 
    return value.replace(u'，', '');

@register.filter
def timeblank(value): 
    return value.replace(' ', '');

@register.filter
def time_chinese_month(value): 
    return value.replace('month', u'月');

@register.filter
def time_chinese_months(value): 
    return value.replace('months', u'月');

@register.filter
def AnonymousUser(value): 
    return value.replace('AnonymousUser', u'游客');

@register.filter
def AtWhoUser(value): 
    commmentdecode = value.decode("utf8")
    pattern = re.compile(u'@([\u4e00-\u9fa5\w\-]+)')  
    results =  pattern.findall(commmentdecode) 
    userlist = []
    print 'for item in userlist:'
    print 'for item in userlist:'
    for item in results:
        user = MyUser.objects.filter(username = item.encode('utf8'))
        if user:
            #notify.send(sender=sender, target_object=targetcomment, recipient = user, verb="@", text=text)
            userlist.append(item.encode('utf8'))
    for item in userlist:
        print 'for item in userlist:'
        atwhouser = MyUser.objects.get(username = item)
        print 'for item in userlist:'
        test = "@<a href='" +'/user/'+str(atwhouser.id)+'/informations/'+"'>"+atwhouser.username+"</a>"+' '
        print 'for item in userlist:'
        value = value.replace('@'+item+' ', test);
        print 'for item in userlist:'
    return value