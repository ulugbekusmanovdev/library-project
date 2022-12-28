from django.contrib import admin
from .models import Ads, Library, Photo, Catalog, Video

# Register your models here.


class LibraryAdm(admin.ModelAdmin):
    list_display = ('id', 'l_title', 'm_title', 'os_title')


admin.site.register(Ads)
admin.site.register(Library, LibraryAdm)
admin.site.register(Photo)
admin.site.register(Catalog)
admin.site.register(Video)