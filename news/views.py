from django.shortcuts import render, redirect
from .models import News
from .forms import NewsForm

# Create your views here.

def news(request):
    posts = News.objects.all()
    context = {'posts': posts}
    return render(request, 'news.html', context)

def newsOnly(request, pk):
    post = News.objects.get(id=pk)
    context = {'post': post}
    return render(request, 'newsOnly.html', context)


def deletePost(request, pk):
    item = News.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        return redirect('/')

    context = {'item': item}
    return render(request, 'deletepost.html', context)


def updatePost(request, pk):
    news_task = News.objects.get(id=pk)

    form = NewsForm(instance=news_task)
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES, instance=news_task)
        if form.is_valid():
            form.save()
        return redirect('home')

    context = {'form': form}

    return render(request, 'updatepost.html', context)