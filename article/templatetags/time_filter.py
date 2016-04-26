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
from django.core.cache import cache
from article.models import Article

#楼层计算器
@register.filter
def pageaculate(value, arg): 
    return value + (arg-1)*5;

@register.filter
def time_blank_n(value): 
    return value.replace('&nbsp;', '');

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
def Article_readers(value): 
    cachekey = "article_readers_" + str(value)
    article_readers = cache.get(cachekey)
    if article_readers:
        return article_readers
    else:
        article = Article.objects.get(id=value)
        article_readers = article.readers
        cache.set(cachekey, article_readers)
        return cache.get(cachekey)

@register.filter
def Article_comment(value): 
    cachekey = "article_comment_" + str(value)
    if cache.get(cachekey):
        return cache.get(cachekey)
    else:
        article = Article.objects.get(id=value)
        cache.set(cachekey, article.comment_set.count())
        return cache.get(cachekey)

@register.filter
def Article_collection(value): 
    cachekey = "article_collection_" + str(value)
    if cache.get(cachekey):
        return cache.get(cachekey)
    else:
        article = Article.objects.get(id=value)
        cache.set(cachekey,  article.collection_set.count())
        return cache.get(cachekey)

@register.filter
def AtWhoUser(value): 
    commmentdecode = value.decode("utf8")
    pattern = re.compile(u'@([\u4e00-\u9fa5\w\-]+)')  
    results =  pattern.findall(commmentdecode) 
    userlist = []
    for item in results:
        user = MyUser.objects.filter(username = item.encode('utf8'))
        if user:
            #notify.send(sender=sender, target_object=targetcomment, recipient = user, verb="@", text=text)
            userlist.append(item.encode('utf8'))
    for item in userlist:
        atwhouser = MyUser.objects.get(username = item)
        test = "@<a href='" +'/user/'+str(atwhouser.id)+'/informations/'+"'>"+atwhouser.username+"</a>"+' '
        value = value.replace('@'+item+' ', test);
    return value


#显示包含搜索词的句子在页面上
@register.filter
def search(value): 
    value = value.lower()
    search_word = cache.get("search_word").lower()
    search_word = search_word.split()
    try:
        x =  value.find(search_word[0]);
    except:
        x = False;
    try:#第二个搜索词的位置
        y =  value.find(search_word[1])
    except:
        y = False
    if x and y:#显示两个搜索词之间的内容
        if x > y and y-25 >= 0:
            return value[y-25:x+15]+ '...'
        if x > y and y-25 < 0:
            return value[0:x+15]+ '...'    
        if x < y and x-25 >= 0:
            return value[x-25:y+15]+ '...'
        if x < y and x-25 < 0:
            return value[0:y+50]+ '...'
    if x:
        if x-50 >= 0:
            return value[x-25:x+25]+ '...'
        else:
            return value[0:50]+ '...'
    else:
        return value[0:50]+ '...'



#highlight the search_word
@register.filter
def highlight(value): 
    search_word = cache.get("search_word").lower()  
    search_word = search_word.split()
    print search_word
    for item in search_word:
        test = '<font color=red>'+item+'</font>'
        value = value.lower().replace(item, test);
    print 'ok'
    return value