from django.contrib import admin


# Register your models here.

from .models import Group, Topic

class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','timestamp')

class TopicAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','timestamp')


admin.site.register(Group, GroupAdmin)
admin.site.register(Topic, TopicAdmin)

