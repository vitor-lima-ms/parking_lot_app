from django.urls import path
from core import views

app_name = 'core'

urlpatterns = [
    path('pre_finish/<int:parking_space_id>', views.pre_finish, name='pre_finish'),
    path('finish/<int:parking_space_id>/<int:vehicle_id>', views.finish, name='finish'),
    path('', views.index, name='index'),
]
