from rest_framework import serializers
from PlantBuddy.models import DeviceModel, ServiceModel, GatewayModel, ConnectionModel


class DeviceSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    device_name = serializers.CharField()
    latitude = serializers.IntegerField()
    longitude = serializers.IntegerField()
    altitude = serializers.IntegerField()
    location = serializers.CharField()

    def create(self, validated_data):
        return DeviceModel.objects.create(**validated_data)


class ServiceSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    time = serializers.TimeField()
    status = serializers.IntegerField()
    water_ml = serializers.IntegerField()
    countdown_timer = serializers.IntegerField()
    water_counter = serializers.IntegerField()
    voltage_max = serializers.IntegerField()
    voltage_min = serializers.IntegerField()
    current_max = serializers.IntegerField()
    current_min = serializers.IntegerField()
    device_id = serializers.IntegerField(read_only=True)

    def create(self, validated_data):
        return ServiceModel.objects.create(**validated_data)


class GatewaySerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    gtw_network_id = serializers.CharField()
    latitude = serializers.IntegerField()
    longitude = serializers.IntegerField()
    altitude = serializers.IntegerField()
    location = serializers.CharField()

    def create(self, validated_data):
        return GatewayModel.objects.create(**validated_data)


class ConnectionSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    gateway_id = serializers.IntegerField(read_only=True)
    service_id = serializers.IntegerField(read_only=True)
    device_id = serializers.IntegerField(read_only=True)
    rssi = serializers.IntegerField()
    snr = serializers.IntegerField()

    def create(self, validated_data):
        return ConnectionModel.objects.create(**validated_data)
