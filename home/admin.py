from django.contrib import admin
from .models import *


# Register your models here.


class LibraryAdm(admin.ModelAdmin):
    list_display = ('id', 'l_title', 'm_title', 'os_title')


class PostImageAdmin(admin.StackedInline):
    model = PostImage


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    inlines = [PostImageAdmin]

    class Meta:
        model = Photo


@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass


admin.site.register(Ads)
admin.site.register(Library, LibraryAdm)
admin.site.register(Catalog)
admin.site.register(Video)
admin.site.register(Readers)
admin.site.register(Contact)
admin.site.register(Newspaper)
admin.site.register(Journal)
