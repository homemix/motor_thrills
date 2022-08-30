from django.shortcuts import render


def index(request):
    return render(request, 'index.html', {'page_title': 'Home'})


def list_cars(request):
    return render(request, 'cars.html', {'page_title': 'Cars'})


def about_us(request):
    return render(request, 'about.html', {'page_title': 'About us'})


def contact_us(request):
    return render(request, 'contact.html', {'page_title': 'ContactUs'})
