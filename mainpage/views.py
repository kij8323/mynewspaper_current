from django.shortcuts import render
from article.models import Article
# Create your views here.



def home(request):
	queryset = Article.objects.all()
	print queryset
	context = {'queryset': queryset}
	return render(request, 'home.html', context)
	#return render(request, 'home.html')