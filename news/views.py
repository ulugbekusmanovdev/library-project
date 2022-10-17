from django.shortcuts import render
from .models import News

# Create your views here.

def news(request):
    posts = News.objects.all()
    context = {'posts': posts}
    return render(request, 'news.html', context)

def newsOnly(request, pk):
    post = News.objects.get(id=pk)
    context = {'post': post}
    return render(request, 'newsOnly.html', context) 