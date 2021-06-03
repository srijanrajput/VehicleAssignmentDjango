from rest_framework import serializers

from vehicleAPI.models import Vehicle, VehicleDistanceLog


class VehicleDistanceLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = VehicleDistanceLog
        fields = '__all__'

class VehicleSerializer(serializers.ModelSerializer):
    distances = serializers.StringRelatedField(many=True)
    class Meta:
        model = Vehicle
        depth = 2
        fields = ('Unit', 'Mileage', 'Manufacturer', 'status', 'distances')
