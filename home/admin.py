from django.contrib import admin
from .models import Ads, Library, Photo

# Register your models here.

admin.site.register(Ads)
admin.site.register(Library)
admin.site.register(Photo)