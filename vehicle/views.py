from django.views.generic.edit import FormView
from vehicle.my_forms import VehicleRegisterForm, VehicleSearchForm
from vehicle.models import Vehicle
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib import messages

# Create your views here.

"""View that allows create instances of Vehicle and assign drivers"""
class VehicleRegisterFormView(FormView):
    template_name = 'vehicle_register_form.html'
    form_class = VehicleRegisterForm

def saving_vehicle(request):
    form = VehicleRegisterForm(request.POST)
    
    if form.is_valid():
        try:
            vehicle = get_list_or_404(Vehicle, vehicle_plate=form.cleaned_data['vehicle_plate'])
            if len(vehicle) >= 1:
                return render(request, 'vehicle_register_form.html', {'error': 'Automóvel já cadastrado!'})
        except:
            Vehicle.objects.create(
                model=form.cleaned_data['model'],
                vehicle_plate=form.cleaned_data['vehicle_plate'],
            )
            
            return redirect('vehicle:registered_vehicle')

"""Here we see all registered vehicles"""
def registered_vehicle(request):
    form = VehicleSearchForm()
    all_registered_vehicles = Vehicle.objects.all()

    return render(request, 'registered_vehicles.html', {
        'form': form,
        'all_registered_vehicles': all_registered_vehicles,
    })

"""View that allows delete a vehicle by plate"""
def delete_vehicle(request, id):
    vehicle = get_object_or_404(Vehicle, id=id)
    vehicle.delete()
    
    return redirect('vehicle:registered_vehicle')

"""View that displays only vehicle that match the search by plate"""
def plate_search(request):
    form = VehicleSearchForm(request.POST)

    if form.is_valid():
        vehicle = get_object_or_404(Vehicle, vehicle_plate=form.cleaned_data['plate_search'])

        return render(request, 'plate_search.html', {'vehicle': vehicle})