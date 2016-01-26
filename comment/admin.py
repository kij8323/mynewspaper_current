from django.contrib import admin

# Register your models here.

from .models import Comment

class CommentAdmin(admin.ModelAdmin):
	list_display = ('id', '__unicode__', 'text', 'timestamp')
	class Meta:
		model = Comment



admin.site.register(Comment, CommentAdmin)
