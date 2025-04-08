from django.db import models
from driver.models import Driver

# Create your models here.

class Vehicle(models.Model):
    driver = models.ForeignKey(
        Driver,
        blank=True,
        null=True,
        default=None,
        on_delete=models.SET_DEFAULT,
    )
    model = models.CharField(max_length=50)
    vehicle_plate = models.CharField(max_length=7)
    checkin_datetime = models.DateTimeField(auto_now=True)
    parked = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.model} - {self.vehicle_plate}'