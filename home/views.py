from django.shortcuts import render
from .models import Ads, Photo, Library, Video
from news.models import News
from libraries.decorators import allowed_users


# Create your views here.
# @allowed_users(allowed_roles=['admin'])
def home(request):
    posts = News.objects.order_by('-create_date')[0:3]
    ads = Ads.objects.order_by('-id')[0:4]
    photos = Photo.objects.order_by('-id')[0:4]
    videos = Video.objects.order_by('-id')[0:4]
    h_news = News.objects.all().first()
    post = News.objects.all()
    context = {'posts': posts, 'ads': ads, 'photos': photos, 'videos': videos, 'h_news': h_news, 'post': post}
    return render(request, 'home.html', context)


def about(request):
    library = Library.objects.filter(id=1)
    library2 = Library.objects.filter(id=2)
    library4 = Library.objects.filter(id=4)
    library5 = Library.objects.filter(id=5)
    context = {'library2': library2, 'library': library, 'library4': library4, 'library5': library5}
    return render(request, 'about.html', context)


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


def structure(request):
    return render(request, 'structure.html')


def photo(request):
    if request.method == 'POST':
        photos = request.FILES.getlist('images')
        for image in photos:
            Photo.objects.create(photos=image)
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
    videos = Video.objects.all()
    return render(request, 'video.html', {'videos': videos})


def videoOnly(request):

    return render(request, 'videoOnly.html')