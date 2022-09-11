from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import *
from .forms import NewUserForm, ReviewForm
from django.contrib import messages


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
    vehicle_company = Company.objects.all()

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
        vehicle_name = self.request.GET.get('vehicle_name')

        if make:
            return Vehicle.objects.filter(make__exact=make)
        elif YOM:
            return Vehicle.objects.filter(YOM__exact=YOM)
        elif company:
            return Vehicle.objects.filter(company_id=company)
        elif vehicle_name:
            return Vehicle.objects.filter(name__iregex=vehicle_name)
        else:
            return Vehicle.objects.order_by('-YOM')


def about_us(request):
    vehicles_count = Vehicle.objects.count()
    make_count = Vehicle.objects.values_list('make', flat=True).distinct().count()
    company_count = Company.objects.count()
    review_form = ReviewForm()
    reviews = Review.objects.all()

    if request.method == 'POST' and request.user.is_authenticated:
        user = request.user
        rating = request.POST.get('rating')
        review = request.POST.get('review')
        data = Review(user=user, rating=rating, review=review)
        data.save()
        return redirect('webapp:about_us')
    else:
        messages.error(request, 'Please login to submit review')


    return render(request, 'about.html', {
        'page_title': 'About us',
        'vehicles_count': vehicles_count,
        'make_count': make_count,
        'company_count': company_count,
        'review_form': review_form,
        'reviews': reviews,

    })


def contact_us(request):
    return render(request, 'contact.html', {'page_title': 'ContactUs'})


def register_user(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('webapp:cars')
    else:
        form = NewUserForm()

    return render(request, 'registration/register.html', {
        'page_title': 'Register',
        'form': form,
    })
