from django.contrib import admin
from vehicle.models import Vehicle

# Register your models here.

@admin.register(Vehicle)
class VehicleAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'model',
        'vehicle_plate',
    ]

    class Meta:
        ordering = (('-checkin_datetime',))