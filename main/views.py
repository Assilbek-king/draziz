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
    prices = Price.objects.all()
    return render(request, 'price.htm', {
        'otzivs': otzivs,
        'prices': prices,
    })

def serviceHandler(request):
    otzivs = Otziv.objects.all()
    return render(request, 'service.html', {
        'otzivs':otzivs,
    })

def contactHandler(request):

    return render(request, 'contact.htm', {
    })

def appointHandler(request):
    if request.POST:
        new_zapis = Zapis()
        new_zapis.name = request.POST.get('name', '')
        new_zapis.phone = request.POST.get('phone', '')
        new_zapis.service = request.POST.get('service', '')
        new_zapis.date = request.POST.get('date', '')
        new_zapis.save()




    return render(request, 'contact.htm', {
    })