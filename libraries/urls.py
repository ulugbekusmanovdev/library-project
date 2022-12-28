from django.urls import path
from . import views

urlpatterns = [
    path('', views.forLibrarists, name='forLibrarists'),
    path('readers', views.readers, name='readers'),
    path('direction', views.direction, name='direction'),
    path('good_to_know', views.good_to_know, name='good_to_know'),
    path('library_entry', views.library_entry, name='library_entry'),
    path('reading_rooms', views.reading_rooms, name='reading_rooms'),
    path('subscription', views.subscription, name='subscription'),
    path('work_schedule', views.work_schedule, name='work_schedule'),
    path('register', views.registerUser, name='register'),
    path('login', views.loginUser, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('infoLib', views.infoLib, name='infoLib'),
    path('videoLib', views.videoLib, name='videoLib'),
    path('add-book', views.addBook, name='add-book'),
    path('search', views.search, name='search'),
    path('books', views.books, name='books'),
    path('chatform', views.chatForm, name='chatform'),
    path('chat', views.chat, name='chat'),
]


