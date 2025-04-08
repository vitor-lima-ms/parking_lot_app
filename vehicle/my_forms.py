from django import forms
from driver.models import Driver

"""Form to create instances of the Vehicle model and assign drivers"""
class VehicleRegisterForm(forms.Form):
    model = forms.CharField(max_length=50)
    vehicle_plate = forms.CharField(max_length=7)

"""Form to search for vehicle by name"""
class VehicleSearchForm(forms.Form):
    plate_search = forms.CharField(max_length=7)