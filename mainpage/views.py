from django.shortcuts import render
from article.models import Article, Category
# Create your views here.



def home(request):
	queryset = Article.objects.all()
	#category = Category.objects.all()
	#print category
	print queryset
	context = {
	'queryset': queryset,
	#'category': category,
	}
	return render(request, 'home.html', context)
	#return render(request, 'home.html')