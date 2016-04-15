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


    # url(r'^test/', 'article.views.test', name='test'),
    #登录页面
    url(r'^user/loggin/', 'accounts.views.loggin', name='loggin'),
    url(r'^user/userlogout/', 'accounts.views.userlogout', name='userlogout'),
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
    url(r'^user/(?P<user_id>[0-9]+)/privcynotifications/$', 'accounts.views.privcynotifications', name='user_privcynotifications'),
    url(r'^user/(?P<user_id>[0-9]+)/collections/$', 'accounts.views.userdashboardcollections', name='user_detailcollections'),
    url(r'^user/(?P<user_id>[0-9]+)/collectionstopic/$', 'accounts.views.userdashboardcollectionstopic', name='user_detailcollectionstopic'),
    url(r'^user/(?P<user_id>[0-9]+)/article/$', 'accounts.views.userdashboardarticle', name='user_userdashboardarticle'),
    url(r'^user/(?P<user_id>[0-9]+)/articletopic/$', 'accounts.views.userdashboardarticletopic', name='user_userdashboardarticletopic'),
    url(r'^user/(?P<user_id>[0-9]+)/userdashboard_commentocomment/$', 'accounts.views.userdashboard_commentocomment', name='userdashboard_commentocomment'),
    url(r'^user/deleteinfo/$', 'accounts.views.deleteinfo', name='deleteinfo'),


    url(r'^group/index/$', 'topic.views.group_index', name='group_index'),
    url(r'^group/all/$', 'topic.views.group_all', name='group_all'),
    url(r'^group/(?P<group_id>[0-9]+)/$', 'topic.views.group_detail', name='group_detail'),
    url(r'^topic/(?P<topic_id>[0-9]+)/$', 'topic.views.topic_detail', name='topic_detail'),
    url(r'^topic/newtopic/$', 'topic.views.newtopic', name='newtopic'),
    url(r'^topic/topicomment/$', 'topic.views.topicomment', name='topicomment'),
    url(r'^topic/topcommentcomment/$', 'topic.views.topcommentcomment', name='topcommentcomment'),
    url(r'^topic/atwhoidentify/$', 'topic.views.atwhoidentify', name='atwhoidentify'),
    url(r'^topic/moretopic/$', 'topic.views.moretopic', name='moretopic'),
    url(r'^topic/groupage/$', 'topic.views.groupage', name='groupage'),
    url(r'^topic/collectiontopic/$', 'topic.views.collectiontopic', name='collectiontopic'),


    url(r'^articlecomment/$', 'article.views.articlecomment', name='articlecomment'),
    url(r'^commentcomment/$', 'article.views.commentcomment', name='commentcomment'),
    url(r'^morecomment/$', 'article.views.morecomment', name='morecomment'),
    url(r'^category/(?P<category_id>[0-9]+)/$', 'article.views.category_detail', name='category_detail'),
    url(r'^category/morearticleincat/$', 'article.views.morearticleincat', name='morearticleincat'),
    url(r'^category/articlepage/$', 'article.views.articlepage', name='articlepage'),
    #ajax，验证用户名是否已被注册,get
    #url(r'^usernamemessage/$', 'accounts.views.usernamemessage', name='usernamemessage'),
        #具体文章页面
    url(r'^article/(?P<article_id>[0-9]+)/$', 'article.views.article_detail', name='article_detail'),
    url(r'^article/commentpage/(?P<article_id>[0-9]+)/$', 'article.views.commentpage', name='commentpage'),
    url(r'^article/collection/$', 'article.views.collection', name='collection'),
    url(r'^article/test/$', 'article.views.test', name='test'),
    url(r'^article/commentlike/$', 'article.views.commentlike', name='commentlike'),
    url(r'^article/commentdislike/$', 'article.views.commentdislike', name='commentdislike'),
    url(r'^article/article_post/$', 'article.views.article_post', name='article_post'),


]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)