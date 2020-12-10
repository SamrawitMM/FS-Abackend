from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = (
    (1, 'Driver'),
    (2, 'Passenger'),
    (3, 'Owner'),
    )
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, null = True)
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    # full_name = models.CharField(db_index=True, max_length=255)
    phone_number = models.IntegerField(blank=True,null=True)