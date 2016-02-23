#coding=utf-8
#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django import template
register = template.Library()

@register.filter
def time_chinese_week(value): 
    return value.replace('week', u'星期前');

@register.filter
def time_chinese_weeks(value): 
    return value.replace('weeks', u'星期前');

@register.filter
def time_chinese_minus(value): 
    return value.replace('minutes', u'分钟前');

@register.filter
def time_chinese_minu(value): 
    return value.replace('minute', u'分钟前');

@register.filter
def time_chinese_day(value): 
    return value.replace('day', u'天前');

@register.filter
def time_chinese_days(value): 
    return value.replace('days', u'天前');

@register.filter
def time_chinese_hour(value): 
    return value.replace('hour', u'小时前');

@register.filter
def time_chinese_hours(value): 
    return value.replace('hours', u'小时前');

@register.filter
def timeblank(value): 
    return value.replace(' ', '');

@register.filter
def time_chinese_month(value): 
    return value.replace('month', u'月前');

@register.filter
def time_chinese_months(value): 
    return value.replace('months', u'月前');

@register.filter
def AnonymousUser(value): 
    return value.replace('AnonymousUser', u'游客');