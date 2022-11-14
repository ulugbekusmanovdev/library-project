from django.urls import path
from . import views

urlpatterns = [
    path('', views.news, name='news'),
    path('single_news/<str:pk>', views.newsOnly, name='single-news'),
    path('delete/<str:pk>', views.deletePost, name='delete-post'),
    path('update/<str:pk>', views.updatePost, name='update-post'),
]
