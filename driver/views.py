from django.views.generic.edit import FormView
from driver.my_forms import DriverRegisterForm, DriverSearchForm
from driver.models import Driver
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from base_dir.functions import cpf_validator
from django.db import models
# Create your views here.

"""View that allows create instances of Driver"""
class DriverRegisterFormView(FormView):
    template_name = 'driver_register_form.html'
    form_class = DriverRegisterForm

def saving_driver(request): 
    if request.method == 'POST':
        form = DriverRegisterForm(request.POST, request.FILES)
        
        if 'file_upload' in request.FILES:
            file = request.FILES['file_upload']
        else:
            file = None
        
        if form.is_valid():
            drivers = Driver.objects.filter(Q(cpf=form.cleaned_data['cpf']) | Q(cnh=form.cleaned_data['cnh']))
            
            if len(drivers) >= 1:
                return render(request, 'driver_register_form.html', {'register_error': 'Motorista já cadastrado!'})

            cpf_validation = cpf_validator(form.cleaned_data['cpf'])

            if cpf_validation:
                driver = Driver.objects.create(
                    driver_name=form.cleaned_data['driver_name'],
                    monthly=form.cleaned_data['monthly'],
                    cnh=form.cleaned_data['cnh'],
                    cpf=form.cleaned_data['cpf'],
                    file_upload=file,
                )
                driver.save()
        
                return redirect('driver:registered_drivers')
            
            return render(request, 'driver_register_form.html', {
                'form': form,
                'cpf_error': 'CPF inválido!'
            })
    else:
        form = DriverRegisterForm()
        return render(request, 'driver_register_form.html', {'form': form})

"""Here we see all registered drivers"""
def registered_drivers(request):
    form = DriverSearchForm()
    all_registered_drivers = Driver.objects.all()

    return render(request, 'registered_drivers.html', {
        'form': form,
        'all_registered_drivers': all_registered_drivers,
    })

"""View that allows delete a driver by cpf"""
def delete_drivers(request, cpf):
    driver = get_object_or_404(Driver, cpf=cpf)
    driver.delete()
    return redirect('driver:registered_drivers')

"""View that displays only drivers that match the search by name"""
def driver_search(request):
    form = DriverSearchForm(request.POST)

    if form.is_valid():
        drivers = Driver.objects.filter(driver_name__contains=form.cleaned_data['name_search'])

        return render(request, 'driver_search.html', {'drivers': drivers})