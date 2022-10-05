from django.shortcuts import render
from .models import News

# Create your views here.

def news(request):
    posts = News.objects.all()
    context = {'posts': posts}
    return render(request, 'news.html', context)