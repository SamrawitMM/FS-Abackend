from django.contrib import admin

from .models import TripHistory
from .models import Owner

admin.site.register(TripHistory)
admin.site.register(Owner)

