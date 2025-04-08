from django.urls import path
from driver import views

app_name = 'driver'

urlpatterns = [
    path('register_form', views.DriverRegisterFormView.as_view(), name='driver_register_form'),

    path('saving_driver', views.saving_driver, name='saving_driver'),

    path('registered', views.registered_drivers, name='registered_drivers'),

    path('delete/<str:cpf>', views.delete_drivers, name='delete_drivers'),

    path('search', views.driver_search, name='driver_search'),
]
