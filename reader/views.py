from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .form import CreateUserForm


def registerUser(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            messages.success(request, 'Account was created for ' + username)

            return redirect('login')

    context = {'form': form}
    return render(request, 'register.html', context)


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
                messages.error(request, 'Username or password is incorrect')

    context = {}
    return render(request, 'login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def forLibrarists(request):
    return render(request, 'forLibrarists.html')


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


def register(request):
    return render(request, "register.html")
