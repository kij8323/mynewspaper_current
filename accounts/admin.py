#coding=utf-8
from django.contrib import admin
from .models import MyUser, UserProfile
# from .form import UserChangeForm, UserCreationForm
# Register your models here.

class MyUserAdmin(admin.ModelAdmin):
	# form = UserChangeForm
	# add_form = UserCreationForm
	list_display = ('id', 'username', 'timestamp')

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'company_name')

# class UserConecctionAdmin(admin.ModelAdmin):
#     list_display = ('id', 'user', 'article')

admin.site.register(MyUser, MyUserAdmin)
admin.site.register(UserProfile, UserProfileAdmin)
# admin.site.register(UserConecction, UserConecctionAdmin)