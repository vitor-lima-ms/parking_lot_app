from django.views.generic.edit import FormView
from vehicle.my_forms import VehicleSearchForm
from parking_space.my_forms import ParkingSpaceCreationForm, ParkingAssignmentForm
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from parking_space.models import ParkingSpace
from vehicle.models import Vehicle

# Create your views here.

"""View that allows you to add new parking spaces"""
class ParkingSpaceCreationFormView(FormView):
    template_name = 'parking_creation_form.html'
    form_class = ParkingSpaceCreationForm

"""View that allows you to view the occupancy history of a parking space"""
def parking_space_history(request, parking_space_id):
    form = VehicleSearchForm()
    parking_space = get_object_or_404(ParkingSpace, id=parking_space_id)

    return render(request, 'parking_space_history.html', {'parking_space': parking_space, 'form': form})

"""View that displays only vehicle that match the search by plate, in parking space history"""
def parking_space_history_plate_search(request):
    form = VehicleSearchForm(request.POST)

    if form.is_valid():
        vehicle = get_object_or_404(Vehicle, vehicle_plate=form.cleaned_data['plate_search'])
        plate = vehicle.vehicle_plate
        parking_places = ParkingSpace.objects.all()
        search_result = list()
        for parking_place in parking_places:
            for vehicle in parking_place.history:
                if vehicle['vehicle_plate'] == plate:
                    search_result.append(vehicle)
                    vehicle['parking_place'] = parking_place

        return render(request, 'parking_space_history_plate_search.html', {'search_result': search_result})

"""View that allows assign autos to parking spaces"""
class ParkingAssignmentFormView(FormView):
    template_name = 'parking_assignment_form.html'
    form_class = ParkingAssignmentForm

def saving_parking_place(request):
    form = ParkingAssignmentForm(request.POST)

    if form.is_valid():
        parking_space = get_object_or_404(ParkingSpace, id=form.cleaned_data['parking_places'].id)
        parking_space.occupied = True
        parking_space.occupied_by = form.cleaned_data['occupied_by']
        parking_space.save()
        
        vehicle = get_object_or_404(Vehicle, vehicle_plate=form.cleaned_data['occupied_by'].vehicle_plate)
        vehicle.parked = True
        vehicle.driver = form.cleaned_data['driver']
        vehicle.save()
    
    return redirect('core:index')

"""Here we see all the occupied parking spaces"""
def occupied_parking_spaces(request):
    occupied_parking_spaces = ParkingSpace.objects.filter(occupied=True)

    return render(request, 'occupied_parking_spaces.html', {'occupied_parking_spaces': occupied_parking_spaces})