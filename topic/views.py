from django.shortcuts import render
from django.http import Http404
from .models import Group, Topic

# Create your views here.
def group_detail(request, group_id):
	try:
		group = Group.objects.get(pk=group_id)
		topic = group.topic_set.all()
		context = {
			'group': group,
			"topic": topic,
			}
		print "group_detail"
		print topic
	except group.DoesNotExist:
		raise Http404("Does not exist")
	return render(request, 'group_detail.html',  context)

def topic_detail(request, topic_id):
	try:
		topic = Topic.objects.get(pk=topic_id)
	except topic.DoesNotExist:
		raise Http404("Does not exist")
	return render(request, 'topic_detail.html',  {'topic': topic})