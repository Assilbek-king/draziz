from django.shortcuts import render
from main.models import *

# Create your views here.
def indexHandler(request):
    otzivs = Otziv.objects.all()
    return render(request, 'index.html', {
        'otzivs': otzivs,
    })

def aboutHandler(request):
    doctors = Doctor.objects.filter(status=True)
    return render(request, 'about.html', {
        'doctors': doctors
    })


def priceHandler(request):
    otzivs = Otziv.objects.all()
    return render(request, 'price.htm', {
        'otzivs': otzivs,
    })

def serviceHandler(request):
    otzivs = Otziv.objects.all()
    return render(request, 'service.html', {
        'otzivs':otzivs,
    })

def contactHandler(request):

    return render(request, 'contact.htm', {
    })