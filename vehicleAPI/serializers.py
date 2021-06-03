from rest_framework import serializers

from .models import Vehicle, VehicleDistanceLog

class VehicleDistanceLogSerializer(serializers.ModelSerializer):
    # level = LevelSerializer(read_only=True)

    class Meta:
        model = VehicleDistanceLog
        fields = '__all__'
        # depth = 1
        # fields = ('Unit', 'Mileage', 'Manufacturer', 'status')

class VehicleSerializer(serializers.ModelSerializer):
    level = VehicleDistanceLogSerializer(read_only=True)
    class Meta:
        model = Vehicle
        fields = '__all__'
        # depth = 1
        # fields = ('Unit', 'Mileage', 'Manufacturer', 'status')

