from django.contrib import admin

# Register your models here.

from .models import Vehicle, VehicleDistanceLog

admin.site.register(Vehicle)
admin.site.register(VehicleDistanceLog)