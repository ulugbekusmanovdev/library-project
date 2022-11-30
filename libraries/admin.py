from django.contrib import admin
from .models import Customer, Faculty, Book
# Register your models here.

admin.site.register(Customer)
admin.site.register(Faculty)
admin.site.register(Book)