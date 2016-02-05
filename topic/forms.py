#coding=utf-8
#! /usr/bin/env python
# -*- coding: utf-8 -*-
from django import forms
from ckeditor.fields import RichTextField
from ckeditor.widgets import CKEditorWidget

class TopicForm(forms.Form):
    content = forms.CharField(widget=CKEditorWidget())
    title = forms.CharField(widget=forms.TextInput())

   