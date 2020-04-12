from django.shortcuts import render
from .models import Service, Menu

def service_list(request):
    services = Service.objects.all()
    menu = Menu.objects.all()
    return render(request, 'services/services_list.html', {'services' : services, 'menu' : menu})
