from django.contrib import admin


# Register your models here.

from .models import Group, Topic, CollectionTopic

class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','timestamp')

class TopicAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','timestamp')

class CollectionTopicAdmin(admin.ModelAdmin):
    list_display = ('id', 'user','topic')


admin.site.register(Group, GroupAdmin)
admin.site.register(Topic, TopicAdmin)
admin.site.register(CollectionTopic, CollectionTopicAdmin)

