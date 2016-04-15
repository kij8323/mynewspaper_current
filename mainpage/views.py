from django.shortcuts import render
from article.models import Article, Category
from topic.models import Group, Topic
from comment.models import Comment
import datetime
from datetime import timedelta
# Create your views here.



def home(request):
	coverarticle = Article.objects.all().filter(timestamp__gte=datetime.date.today() - timedelta(days=30)).filter(cover = True).order_by("-timestamp")[0:3]
	covertopic = Topic.objects.all().filter(timestamp__gte=datetime.date.today() - timedelta(days=30)).filter(cover = True).order_by("-timestamp")[0:1]
	print covertopic.count()
	queryset = Article.objects.all().order_by('-timestamp')
	topic = Topic.objects.all().filter(timestamp__gte=datetime.date.today() - timedelta(days=30)).order_by("-readers")[0:5]
	hotnews = Article.objects.all().filter(timestamp__gte=datetime.date.today() - timedelta(days=30)).order_by("-readers")[0:5]
	nicecomment = Comment.objects.all().filter(timestamp__gte=datetime.date.today() - timedelta(days=30)).order_by("-readers")[0:5]
	context = {
	'queryset': queryset,
	'topicquery' : topic,
	'hotnews': hotnews,
	'nicecomment': nicecomment,
	'coverarticle': coverarticle,
	'covertopic': covertopic[0],
	}
	return render(request, 'home.html', context)
	#return render(request, 'home.html')