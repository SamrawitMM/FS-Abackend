from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver
from driver.models import Driver

RIDE_TYPE = (
            ('S','Shared'),
            ('R','Ride')
            )

class Passenger(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name='passenger_profile', blank=True)
    current_latitude = models.FloatField( validators=[MinValueValidator(-180), MaxValueValidator(180)], default=None, null =True)
    current_longitude = models.FloatField( validators=[MinValueValidator(-180), MaxValueValidator(180)], default=None, null= True)
    previous_latitude = models.FloatField( validators=[MinValueValidator(-180), MaxValueValidator(180)], default=None, null= True)
    previous_longitude = models.FloatField( validators=[MinValueValidator(-180), MaxValueValidator(180)], default=None, null = True)

    def __str__(self):
        return self.user.username


class PassengerSchedule(models.Model):
    passenger = models.ForeignKey(Passenger, on_delete=models.CASCADE, null= False)
    driver = models.ForeignKey(Driver, on_delete = models.CASCADE,null=False)
    pick_up_time = models.DateTimeField()
    pick_up_latitude = models.FloatField(validators=[MinValueValidator(-180),
                                  MaxValueValidator(180)])
    pick_up_longitude = models.FloatField( validators=[MinValueValidator(-180),
                                  MaxValueValidator(180)])
    destination_latitude = models.FloatField( validators=[MinValueValidator(-180),
                                  MaxValueValidator(180)])
    destination_longitude = models.FloatField( validators=[MinValueValidator(-180),
                                  MaxValueValidator(180)])
    ride_option = models.CharField(choices = RIDE_TYPE, max_length = 1)
    # CharField(choices=RIDE_TYPE,max_length=1)
    estimated_cost = models.FloatField(validators=[MinValueValidator(0)])
    is_assigned = models.BooleanField(default=False)
    	# models.BooleanField()
    num_of_people = models.IntegerField(validators=[MinValueValidator(1),
                                  MaxValueValidator(4)])
    # passengerId = models.ForeignKey(Passenger, on_delete = models.CASCADE, null = True)

    def __str__(self):
        return self.passenger.user.username + " " + str(self.pick_up_time) 
# # Create your models here.

    # def __str(self):
    #     return self.name
