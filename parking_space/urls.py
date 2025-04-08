from django.urls import path
from parking_space import views

app_name = 'parking_space'

urlpatterns = [
    path('parking_creation_form', views.ParkingSpaceCreationFormView.as_view(), name='parking_creation_form'),

    path('parking_space_history/<int:parking_space_id>', views.parking_space_history, name='parking_space_history'),

    path('parking_space_history/plate_search', views.parking_space_history_plate_search, name='parking_space_history_plate_search'),

    path('parking_assignment_form', views.ParkingAssignmentFormView.as_view(), name='parking_assignment_form'),

    path('saving_parking_place', views.saving_parking_place, name='saving_parking_place'),
    
    path('occupied_parking_spaces', views.occupied_parking_spaces, name='occupied_parking_spaces'),
]
