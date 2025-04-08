from parking_space.my_forms import ParkingSpaceCreationForm
from parking_space.models import ParkingSpace
from vehicle.my_forms import VehicleSearchForm
from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime, timezone
from base_dir.functions import price_calculator
from vehicle.models import Vehicle
from django.contrib import messages

# Create your views here.

"""Main page"""
def index(request):
    form = ParkingSpaceCreationForm(request.POST)

    if form.is_valid():
        for _ in range(form.cleaned_data['qtd']):
            ParkingSpace.objects.create()
    
    parking_spaces = ParkingSpace.objects.filter(occupied=False)

    plate_search = VehicleSearchForm()

    return render(request, 'core_index.html', {'parking_spaces': parking_spaces, 'form': plate_search})

"""In this view, we calculate the amount to be paid and see all relevant information before receiving payment and releasing the parking space"""
def pre_finish(request, parking_space_id):
    parking_space = get_object_or_404(ParkingSpace, id=parking_space_id)
    
    checkin_datetime = parking_space.occupied_by.checkin_datetime
    current_datetime = datetime.now(timezone.utc)

    time_delta = current_datetime - checkin_datetime

    price = round(price_calculator(time_delta), 2)

    fmt_price = f'{price:.2f}'.replace('.', ',')

    if bool(parking_space.occupied_by.driver.monthly) == False:
        return render(request, 'core_pre_finish.html', {
            'monthly': False,
            'parking_space': parking_space,
            'checkin_datetime': checkin_datetime,
            'current_datetime': current_datetime,
            'price': fmt_price,
        })
    
    return render(request, 'core_pre_finish.html', {
            'monthly': True,
            'parking_space': parking_space,
            'checkin_datetime': checkin_datetime,
            'current_datetime': current_datetime,
        })

def finish(request, parking_space_id, vehicle_id):
    parking_space = get_object_or_404(ParkingSpace, id=parking_space_id)
    vehicle = get_object_or_404(Vehicle, id=vehicle_id)

    parking_space.add_history()
    parking_space.remove_auto()
    vehicle.parked = False
    vehicle.driver = None
    vehicle.save()
    parking_space.save()

    messages.success(request, "Saída registrada com sucesso!")

    return redirect('core:index')