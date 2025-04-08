from django.contrib import admin
from parking_space.models import ParkingSpace

# Register your models here.

@admin.register(ParkingSpace)
class ParkingSpaceAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'occupied',
        'occupied_by',
    ]