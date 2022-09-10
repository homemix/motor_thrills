from django.shortcuts import render
from django.views.generic import ListView
from .models import *


def index(request):
    news = News.objects.all()
    vehicle_make = Vehicle.objects.values_list('make', flat=True).distinct()
    vehicle_YOM = Vehicle.objects.values_list('YOM', flat=True).distinct().order_by('-YOM')
    vehicles = Vehicle.objects.order_by('-YOM')[:8]

    return render(request, 'index.html', {
        'page_title': 'Home',
        'news': news,
        'vehicles': vehicles,
        'vehicle_make': vehicle_make,
        'vehicle_YOM': vehicle_YOM,
    })


class VehicleListView(ListView):
    paginate_by = 8
    model = Vehicle
    template_name = 'cars.html'
    context_object_name = 'vehicles'
    title = 'Cars'
    vehicle_make = Vehicle.objects.values_list('make', flat=True).distinct()
    vehicle_YOM = Vehicle.objects.values_list('YOM', flat=True).distinct().order_by('-YOM')
    vehicle_company= Company.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_title'] = self.title
        context['vehicle_make'] = self.vehicle_make
        context['vehicle_YOM'] = self.vehicle_YOM
        context['vehicle_company'] = self.vehicle_company
        return context

    def get_queryset(self):
        make = self.request.GET.get('make')
        YOM = self.request.GET.get('YOM')
        company = self.request.GET.get('company')
        if make:
            return Vehicle.objects.filter(make__exact=make)
        elif YOM:
            return Vehicle.objects.filter(YOM__exact=YOM)
        elif company:
            return Vehicle.objects.filter(company_id=company)
        if make and YOM:
            return Vehicle.objects.filter(make__exact=make, YOM__exact=YOM)
        else:
            return Vehicle.objects.order_by('-YOM')


def about_us(request):
    vehicles_count= Vehicle.objects.count()
    make_count = Vehicle.objects.values_list('make', flat=True).distinct().count()
    company_count = Company.objects.count()
    return render(request, 'about.html', {
        'page_title': 'About us',
        'vehicles_count': vehicles_count,
        'make_count': make_count,
        'company_count': company_count,
    })


def contact_us(request):
    return render(request, 'contact.html', {'page_title': 'ContactUs'})
