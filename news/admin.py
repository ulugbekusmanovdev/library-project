from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import *


# Register your models here.
class NewsAdmin(admin.ModelAdmin):
    list_display =('id', 'title')


admin.site.register(News, NewsAdmin)