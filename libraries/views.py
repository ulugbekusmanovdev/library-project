from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CustomerForm
from .models import Book
from .decorators import unauthenticated_user, allowed_users
from django.contrib.auth.hashers import make_password


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

    context = {'form': form}
    return render(request, 'forLibrarists.html', context)


def direction(request):
    return render(request, 'direction.html')


def good_to_know(request):
    return render(request, 'good_to_know.html')


def library_entry(request):
    return render(request, 'library_entry.html')


def reading_rooms(request):
    return render(request, 'reading_rooms.html')


def subscription(request):
    return render(request, 'subscription.html')


def work_schedule(request):
    return render(request, 'work_schedule.html')


def readers(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'readers.html', context)


def infoLib(request):
    return render(request, 'infoLib.html')


def videoLib(request):
    return render(request, 'videoLib.html')


def addBook(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        year = request.POST['year']
        pdf = request.FILES['pdf']
        photo = request.FILES['photo']
        a = Book(title=title, author=author, year=year, photo=photo, pdf=pdf)
        a.save()
    return render(request, 'addbook.html')
