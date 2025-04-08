from django.urls import path
from vehicle import views

app_name = 'vehicle'

urlpatterns = [
    path('vehicle_register_form', views.VehicleRegisterFormView.as_view(), name='vehicle_register_form'),

    path('saving_vehicle', views.saving_vehicle, name='saving_vehicle'),

    path('registered_vehicle', views.registered_vehicle, name='registered_vehicle'),

    path('delete_vehicle/<int:id>', views.delete_vehicle, name='delete_vehicle'),

    path('plate_search', views.plate_search, name='plate_search'),
]
