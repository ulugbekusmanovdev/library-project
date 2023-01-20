from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from libraries.decorators import allowed_users, admin_only
from django.contrib import messages

from home.models import Readers
from .forms import CustomerForm, ChatForm
from .models import Book, Category, Customer, Chat, Library, Video
from django.db.models import Q
from .decorators import unauthenticated_user, allowed_users
from django.contrib.auth.hashers import make_password
from .utils import searchBooks


@unauthenticated_user
def registerUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password = make_password(password)

        a = User(username=username, password=password)
        a.save()
        messages.success(request, 'Аккаунт создан для ' + username)
        return redirect('login')
    else:
        messages.error(request, 'Registration fail, try again later')
        return render(request, 'register.html')


# def registerUser(request):
#     form = CreateUserForm()
#     if request.method == 'POST':
#         form = CreateUserForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             username = form.cleaned_data.get('username')
#
#             messages.success(request, 'Аккаунт создан для ' + username)
#
#             return redirect('login')
#
#     context = {'form': form}
#     return render(request, 'register.html', context)


@unauthenticated_user
def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if username and password:
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('forLibrarists')
            else:
                messages.error(request, 'Логин или пароль неверeн')

    context = {}
    return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('/')


@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def forLibrarists(request):
    customer = request.user.customer
    form = CustomerForm(instance=customer)

    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES, instance=customer)
        if form.is_valid():
            form.save()

    irbis = Library.objects.all()
    context = {'form': form, 'irbis': irbis}
    return render(request, 'forLibrarists.html', context)


def readers(request):
    category = request.GET.get('category')
    if category == None:
        books = Book.objects.all()
    else:
        books = Book.objects.filter(category__name=category)

    categories = Category.objects.all()

    reader = Readers.objects.all()
    context = {'books': books, 'categories': categories, 'reader': reader}
    return render(request, 'readers.html', context)


def search(request):
    search = request.GET.get('q')
    books = Book.objects.all()
    if search:
        books = books.filter(
            Q(title__icontains=search) |
            Q(author__icontains=search) |
            Q(category__name__icontains=search)
        )
    return render(request, 'books.html', {"books": books})


@login_required(login_url='login')
@admin_only
def infoLib(request):
    customers = Customer.objects.all()
    return render(request, 'infoLib.html', {'customers': customers})


def books(request):
    category = request.GET.get('category')
    if category == None:
        books = Book.objects.all()
    else:
        books = Book.objects.filter(category__name=category)

    categories = Category.objects.all()
    postlar = Paginator(categories, 4)
    page_list = request.GET.get('page')
    page = postlar.get_page(page_list)
    context = {'books': books, 'categories': page}
    return render(request, 'books.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def addBook(request):
    customer = Customer.objects.get(user=request.user)
    books = Book.objects.filter(customer=customer).count()
    books_count = Book.objects.all().count()

    categories = Category.objects.all()

    if request.method == 'POST':
        data = request.POST
        title = request.POST.get('title')
        author = request.POST.get('author')
        year = request.POST.get('year')
        pdf = request.FILES.get('pdf')
        photo = request.FILES.get('photo')

        if data['category'] != 'none':
            category = Category.objects.get(id=data['category'])
        elif data['category_new'] != '':
            category, created = Category.objects.get_or_create(name=data['category_new'])
        else:
            category = None

        book = Book.objects.create(
            category=category,
            photo=photo,
            title=title,
            author=author,
            year=year,
            pdf=pdf,
            customer=customer,
        )
        return redirect('readers')
    context = {'categories': categories, 'books_count': books_count, 'books': books}
    return render(request, 'addbook.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def videoLib(request):
    videolib = Video.objects.all()
    return render(request, "videoLib.html", {"videolib": videolib})


@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def chat(request):
    chat = Chat.objects.all()
    form = ChatForm()
    if request.method == 'POST':
        form = ChatForm(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            # instance.customer = request.user
            instance.customer = Customer.objects.get(user=request.user)
            instance.save()
        return redirect('chat')
    context = {'form': form, 'chat': chat}
    return render(request, 'chat.html', context)

# def chat(request):
#     chat = Chat.objects.all()
#     return render(request, 'chat.html', {'chat': chat})
