from django.db import models
from django.conf import settings
from django.db.models import DecimalField, FloatField
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator
from driver.models import Car, Driver
from passenger.models import Passenger
# from django.contrib.gis.db import models
# from django.contrib.gis.db import models

class Owner(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name='owner_profile', blank=True)
    current_latitude = models.FloatField( validators=[MinValueValidator(-180), MaxValueValidator(180)], default=None, null =True)
    current_longitude = models.FloatField( validators=[MinValueValidator(-180), MaxValueValidator(180)], default=None, null= True)


    def __str__(self):
        return self.user.username

class TripHistory(models.Model):
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    destination_longitude = models.FloatField( validators=[MinValueValidator(-180), MaxValueValidator(180)], default=None)
    destination_latitude = models.FloatField( validators=[MinValueValidator(-180), MaxValueValidator(180)], default=None)
    pickup_longitude= models.FloatField( validators=[MinValueValidator(-180), MaxValueValidator(180)], default=None)
    pickup_latitude=models.FloatField( validators=[MinValueValidator(-180), MaxValueValidator(180)], default=None)
    start_time = models.TimeField()
    end_time = models.TimeField()
    license_plate = models.CharField(max_length=6, unique=True)
    date = models.DateTimeField(default=timezone.now)
    car = models.ForeignKey(Car, on_delete=models.CASCADE, null= True)
    passenger = models.ForeignKey(Passenger,on_delete = models.CASCADE, null=False)
    driver = models.ForeignKey(Driver, on_delete = models.CASCADE, null=False)
    def __str__(self):
        return self.license_plate
