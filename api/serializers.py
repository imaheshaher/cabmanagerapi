from rest_framework import serializers
from .models import Driver,DriverLocation

class DriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = Driver
        fields = "__all__"



class DriverLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriverLocation
        fields = "__all__"


class DriverListSerializer(serializers.Serializer):
    longitude = serializers.DecimalField(max_digits=15,decimal_places=8)
    latitude = serializers.DecimalField(max_digits=15,decimal_places=8)