#coding=utf-8
#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms


#文章页面评论提交表格
class CommentForm(forms.Form):
    commentext = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 
                                    'placeholder': '',
                                    'rows':"8"}),
        error_messages={'required': '请提交您的看法'})







