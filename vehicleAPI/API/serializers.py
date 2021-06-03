from rest_framework import serializers

from vehicleAPI.models import Vehicle, VehicleDistanceLog


class VehicleDistanceLogSerializer(serializers.ModelSerializer):
    # vehicle = serializers.RelatedField(read_only=True)

    class Meta:
        model = VehicleDistanceLog
        fields = '__all__'
        # depth = 1
        # fields = ('Unit', 'distances_set')

class VehicleSerializer(serializers.ModelSerializer):
    # highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')
    distances = serializers.StringRelatedField(many=True)
    # vehicle_distance_log = VehicleDistanceLogSerializer()
    class Meta:
        model = Vehicle
        # fields = '__all__'
        depth = 2
        fields = ('Unit', 'Mileage', 'Manufacturer', 'status', 'distances')
    
    # def create(self, validated_data):
    #     profile_data = validated_data.pop('vehicle_distance_log')
    #     vehicle = Vehicle.objects.create(**validated_data)
    #     VehicleDistanceLog.objects.create(Unit=vehicle, **profile_data)
    #     return vehicle

