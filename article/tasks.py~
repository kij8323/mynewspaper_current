#from celery import task
#coding=utf-8
#! /usr/bin/env python
# -*- coding: utf-8 -*-
#celery消息队列注册的函数
#注册的函数必须放在名为tasks.py的文件中
from celery.decorators import task
#更新数据库readers+1
@task
def readersin(x):
    x.readers+= 1
    x.save()
    return 'readers +1 success!'

#更新数据库readers-1
@task
def readersout(x):
    x.readers-= 1
    x.save()
    return 'readers -1 success!'

#删除数据库中数据
@task
def instancedelete(x):
    x.delete()
    return 'delete success!'

#向数据库中写入数据
@task
def instancesave(x):
    x.save()
    return 'save success!'

#做实验用的函数
@task
def add(x, y):
  return x + y
