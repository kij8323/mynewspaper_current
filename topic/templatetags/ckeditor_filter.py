#coding=utf-8
#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django import template
register = template.Library()


#无效的代码
@register.filter
def htmltranstlate(value): 
    return value.replace('&', '&amp;');
