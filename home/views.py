from django.shortcuts import render
from .models import Ads, Photo
from news.models import News
from libraries.decorators import allowed_users


# Create your views here.
# @allowed_users(allowed_roles=['admin'])
def home(request):
    posts = News.objects.order_by('-create_date')[0:3]
    ads = Ads.objects.order_by('-id')[0:4]
    photos = Photo.objects.order_by('-id')[0:4]
    context = {'posts': posts, 'ads': ads, 'photos': photos}
    return render(request, 'home.html', context)


def about(request):
    return render(request, 'about.html')


def adt(request):
    ads = Ads.objects.all()
    context = {'ads': ads}
    return render(request, 'adt.html', context)


def catalogs(request):
    return render(request, 'catalogs.html')


def collection(request):
    return render(request, 'collection.html')


def contact(request):
    return render(request, 'contact.html')


def history(request):
    return render(request, 'history.html')


def vacancy(request):
    return render(request, 'vacancy.html')


def structure(request):
    return render(request, 'structure.html')


def photo(request):
    photos = Photo.objects.all()
    context = {'photos': photos}
    return render(request, 'photo.html', context)


def photoOnly(request, pk):
    photos = Photo.objects.all()
    photo = Photo.objects.get(id=pk)
    context = {'photo': photo, 'photos': photos}
    return render(request, 'photoOnly.html', context)


def mission(request):
    return render(request, 'mission.html')


def video(request):
    return render(request, 'video.html')


def videoOnly(request):
    return render(request, 'videoOnly.html')
