from django.contrib import admin
from .models import Car
from .models import Notification, Driver

admin.site.register(Car)
admin.site.register(Notification)
admin.site.register(Driver)
