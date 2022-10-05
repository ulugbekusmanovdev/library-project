from django.shortcuts import render


# Create your views here.

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
