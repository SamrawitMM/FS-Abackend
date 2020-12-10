from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver

class Driver(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name='driver_profile', blank=True)
    rate = models.IntegerField(default = 0)
    status = models.BooleanField(default = True)
    current_latitude = models.FloatField( validators=[MinValueValidator(-180), MaxValueValidator(180)], default=None, null =True)
    current_longitude = models.FloatField( validators=[MinValueValidator(-180), MaxValueValidator(180)], default=None, null= True)
    previous_latitude = models.FloatField( validators=[MinValueValidator(-180), MaxValueValidator(180)], default=None, null= True)
    previous_longitude = models.FloatField( validators=[MinValueValidator(-180), MaxValueValidator(180)], default=None, null = True)

    def __str__(self):
        return self.user.username

class Notification(models.Model):
    case = models.CharField(max_length=50)
    reason = models.TextField()
    is_accepted = models.BooleanField(default = True)
    driver = models.ForeignKey(Driver, on_delete= models.CASCADE, null=True)
    def str(self):
        return self.case

class Car(models.Model):
    CAR_MODEL = (
        ('Cor', 'Corolla'),
        ('Vit','Vitz'),
        ('Yar','Yaris'),
        ('Cad','Cadillac'),
        ('Mer','Mercedes'),
        ('Suz','Suzuki'),
        ('Lif','Lifan'),
        ('For','Ford'),
        ('Kia','Kia'),
        ('BMW','BMW'),
        ('Toy','Toyota'),
        ('Vol','Volkswagen'),
        ('Nis','Nissan'),
        ('Peu','Peugeot')
    )
    car_model = models.CharField(max_length=4, choices = CAR_MODEL)
    is_avaliable = models.BooleanField(default = True)
    license_plate = models.CharField(max_length = 6, unique = True, default = None)
    num_of_seats = models.IntegerField(default=2,
        validators=[
            MinValueValidator(2),
            MaxValueValidator(7)
            ]
            )
    driver = models.ForeignKey(Driver, on_delete= models.CASCADE, null=True)

    def str(self):
        return self.license_plate