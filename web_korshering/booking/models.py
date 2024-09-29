from django.db import models
from django.contrib.auth.models import User

class Vehicle(models.Model):
    TYPE_CHOICES = [
        ('car', 'Car'),
        ('bike', 'Bike'),
        ('scooter', 'Scooter'),
    ]
    name = models.CharField(max_length=100)
    vehicle_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    is_available = models.BooleanField(default=True)
    price_per_hour = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.name

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user} - {self.vehicle} ({self.start_time} - {self.end_time})"

