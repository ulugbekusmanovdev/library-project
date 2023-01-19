from django.contrib import admin
from django.contrib.admin import ModelAdmin
from modeltranslation.admin import TranslationAdmin
from .models import *


# Register your models here.
class NewsAdmin(ModelAdmin):
    fields =['']


admin.site.register(News)