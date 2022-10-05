from django.shortcuts import render
from news.models import News
from news.models import News

# Create your views here.

def home(request):
    posts = News.objects.all()
    context = {'posts': posts}
    return render(request, 'home.html', context)

def about(request):
    return render(request, 'about.html')

def adt(request):
    return render(request, 'adt.html')

def catalogs(request):
    return render(request, 'catalogs.html')

def collection(request):
    return render(request, 'collection.html')


def contact(request):
    return render(request, 'contact.html')


def history(request):
    return render(request, 'history.html')

def forLibrarists(request):
    return render(request, 'forLibrarists.html')

def vacancy(request):
    return render(request, 'vacancy.html')

def structure(request):
    return render(request, 'structure.html')

def photo(request):
    return render(request, 'photo.html')

def mission(request):
    return render(request, 'mission.html')

def video(request):
    return render(request, 'video.html')