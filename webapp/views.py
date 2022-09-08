from django.shortcuts import render
from django.views.generic import ListView
from .models import *


def index(request):
    news = News.objects.all()
    vehicles = Vehicle.objects.order_by('-YOM')[:8]

    return render(request, 'index.html', {
        'page_title': 'Home',
        'news': news,
        'vehicles': vehicles,
    })


def list_cars(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'cars.html', {
        'page_title': 'Cars',
        'vehicles': vehicles
    })


class VehicleListView(ListView):
    paginate_by = 8
    model = Vehicle
    template_name = 'cars.html'
    context_object_name = 'vehicles'
    title = 'Cars'
    vehicle_make = Vehicle.objects.values_list('make', flat=True).distinct()
    vehicle_YOM = Vehicle.objects.values_list('YOM', flat=True).distinct()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = self.title
        context['vehicle_make'] = self.vehicle_make
        context['vehicle_YOM'] = self.vehicle_YOM
        return context

    def get_queryset(self):
        make = self.request.GET.get('make')
        YOM = self.request.GET.get('YOM')
        if make:
            return Vehicle.objects.filter(make__icontains=make)
        elif YOM:
            return Vehicle.objects.filter(YOM__icontains=YOM)
        return Vehicle.objects.order_by('-YOM')


def about_us(request):
    return render(request, 'about.html', {'page_title': 'About us'})


def contact_us(request):
    return render(request, 'contact.html', {'page_title': 'ContactUs'})
