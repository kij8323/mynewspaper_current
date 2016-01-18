#coding=utf-8
#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django import template
register = template.Library()


#无效的代码
@register.filter
def time_chinese_week(value): 
    return value.replace('This field is required.', u'星期');
