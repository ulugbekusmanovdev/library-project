from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import CreateUserForm, CustomerForm
from .decorators import unauthenticated_user, allowed_users


@unauthenticated_user
def registerUser(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            messages.success(request, 'Аккаунт создан для ' + username)

            return redirect('login')

    context = {'form': form}
    return render(request, 'register.html', context)


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
    return render(request, 'readers.html')

def infoLib(request):
    return render(request, 'infoLib.html')

def videoLib(request):
    return render(request, 'videoLib.html')

