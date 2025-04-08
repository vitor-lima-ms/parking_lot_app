from django import forms
from parking_space.models import ParkingSpace
from vehicle.models import Vehicle
from driver.models import Driver

"""Allows you to create new parking spaces"""
CHOICES_LIST = list()
for i in range(1, 101):
    CHOICES_LIST.append((i, str(i)))

class ParkingSpaceCreationForm(forms.Form):
    qtd = forms.TypedChoiceField(choices=CHOICES_LIST, coerce=int)

"""Form to assign autos to parking spaces"""
class ParkingAssignmentForm(forms.Form):
    parking_places = forms.ModelChoiceField(
        ParkingSpace.objects.filter(occupied=False)
    )
    occupied = forms.BooleanField()
    occupied_by = forms.ModelChoiceField(
        Vehicle.objects.filter(parked=False),
        to_field_name='model'
    )
    driver = forms.ModelChoiceField(
        Driver.objects.all(),
        to_field_name='driver_name',
    )