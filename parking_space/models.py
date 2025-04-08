from django.db import models
from vehicle.models import Vehicle
from datetime import datetime, timezone, timedelta

# Create your models here.

"""Model representing parking spaces"""
class ParkingSpace(models.Model):
    occupied = models.BooleanField(default=False)
    occupied_by = models.OneToOneField(
        Vehicle,
        null=True,
        default=None,
        on_delete=models.SET_NULL       
    )
    def create_list():
        return list({})

    history = models.JSONField(default=create_list, null=True)

    def __str__(self):
        if self.id < 10:
            return f'Vaga 00{self.id}'
        elif self.id < 100:
            return f'Vaga 0{self.id}'
        return f'Vaga {self.id}'
        
    
    """Function to remove a veichle in a parking space"""
    def remove_auto(self):
        self.occupied = False
        self.occupied_by = None
    
    """Function to create the history of the parking space"""
    def add_history(self):
        current_datetime = datetime.now(timezone(timedelta(hours=-3)))
        occupied_by = self.occupied_by
        driver = self.occupied_by.driver
        vehicle_plate = self.occupied_by.vehicle_plate
        checkin_datetime = self.occupied_by.checkin_datetime - timedelta(hours=3) # -3 because Brazilian time is 3 hours behind UTC
        total_time = current_datetime - self.occupied_by.checkin_datetime

        self.history.append({
            'model': str(occupied_by),
            'driver': str(driver),
            'vehicle_plate': str(vehicle_plate),
            'checkin_datetime': str(checkin_datetime.strftime('%d/%m/%Y - %H:%M:%S')),
            'checkout_datetime': str(current_datetime.strftime('%d/%m/%Y - %H:%M:%S')),
            'total_time': str(total_time),
        })