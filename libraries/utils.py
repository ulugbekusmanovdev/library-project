from .models import Book, Category
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


def searchBooks(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    books = Book.objects.distinct().filter(
        Q(title__icontains=search_query) |
        Q(author__icontains=search_query) |
        Q(category__name__icontains=search_query)
    )
    return books, search_query
