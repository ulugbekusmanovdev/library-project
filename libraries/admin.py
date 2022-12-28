from django.contrib import admin
from .models import Customer, Faculty, Book, Category, Chat
# Register your models here.

admin.site.register(Customer)
admin.site.register(Faculty)
admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Chat)