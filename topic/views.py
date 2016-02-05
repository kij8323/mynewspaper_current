from django.shortcuts import render, redirect
from django.http import Http404
from .models import Group, Topic, TopicForm

# from .forms import TopicForm

# Create your views here.
def group_detail(request, group_id):
	try:
		group = Group.objects.get(pk=group_id)
		topic = group.topic_set.all()
		context = {
			'group': group,
			'topic': topic,
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

def newtopic(request):
	if request.method == 'POST':
		form = TopicForm(request.POST)
		if form.is_valid():
			content = form.cleaned_data['content']
			title = form.cleaned_data['title']
			new_topic = Topic()
			new_topic.content = content
			new_topic.title = title
			new_topic.writer = request.user
			new_topic.group = Group.objects.get(pk=1)
			new_topic.save()
			return redirect('newtopic')
	else:
		print  request.user
		context = {
			'myform': TopicForm,
			}
	return render(request, 'newtopic.html',  context)