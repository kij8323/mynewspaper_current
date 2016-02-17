#coding=utf-8
#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    #主页
    url(r'^$', 'mainpage.views.home', name='home'),


    url(r'^user/test/', 'accounts.views.test', name='test'),
    #登录页面
    url(r'^user/loggin/', 'accounts.views.loggin', name='loggin'),
    #注册页面
    url(r'^user/register/', 'accounts.views.register', name='register'),
    #登出页面
    url(r'^user/logout/', 'accounts.views.logout_view', name='logout'),
    #ajax我的评论
    url(r'^userdashboard_comment/$', 'accounts.views.userdashboard_comment', name='userdashboard_comment'),
    url(r'^captcha/', include('captcha.urls')),  
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),
    #ajax，验证码刷新
    url(r'^captchaview/$', 'accounts.views.captchaview', name='captchaview'),
    #ajax，验证用户名是否已被注册,post
    url(r'^accountsview/$', 'accounts.views.accountsview', name='accountsview'),
    #用户信息页面
    url(r'^user/(?P<user_id>[0-9]+)/informations/$', 'accounts.views.userdashboardinformations', name='user_detailinformations'),
    url(r'^user/(?P<user_id>[0-9]+)/comments/$', 'accounts.views.userdashboardcomments', name='user_detailcomments'),
    url(r'^user/(?P<user_id>[0-9]+)/notifications/$', 'accounts.views.userdashboardnotifications', name='user_detailnotifications'),
    url(r'^user/(?P<user_id>[0-9]+)/collections/$', 'accounts.views.userdashboardcollections', name='user_detailcollections'),




    url(r'^group/(?P<group_id>[0-9]+)/$', 'topic.views.group_detail', name='group_detail'),
    url(r'^topic/(?P<topic_id>[0-9]+)/$', 'topic.views.topic_detail', name='topic_detail'),
    url(r'^topic/newtopic/$', 'topic.views.newtopic', name='newtopic'),
    url(r'^topic/topicomment/$', 'topic.views.topicomment', name='topicomment'),
    url(r'^topic/topcommentcomment/$', 'topic.views.topcommentcomment', name='topcommentcomment'),





    url(r'^articlecomment/$', 'article.views.articlecomment', name='articlecomment'),
    url(r'^commentcomment/$', 'article.views.commentcomment', name='commentcomment'),
    url(r'^morecomment/$', 'article.views.morecomment', name='morecomment'),
    url(r'^category/(?P<category_id>[0-9]+)/$', 'article.views.category_detail', name='category_detail'),
    #ajax，验证用户名是否已被注册,get
    #url(r'^usernamemessage/$', 'accounts.views.usernamemessage', name='usernamemessage'),
        #具体文章页面
    url(r'^article/(?P<article_id>[0-9]+)/$', 'article.views.article_detail', name='article_detail'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)