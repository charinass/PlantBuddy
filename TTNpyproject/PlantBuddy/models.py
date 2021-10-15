from django.db import models


# Create your models here.
class DeviceModel(models.Model):
    device_name = models.CharField(max_length=20)
    latitude = models.IntegerField(default=None)
    longitude = models.IntegerField(default=None)
    altitude = models.IntegerField(default=None)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.device_name


class ServiceModel(models.Model):
    time = models.TimeField(auto_now_add=False)
    status = models.IntegerField(default=None)
    water_ml = models.IntegerField(default=None)
    countdown_timer = models.IntegerField(default=None)
    water_counter = models.IntegerField(default=None)
    voltage_max = models.IntegerField(default=None)
    voltage_min = models.IntegerField(default=None)
    current_max = models.IntegerField(default=None)
    current_min = models.IntegerField(default=None)
    device_id = models.ForeignKey(DeviceModel, models.CASCADE, null=False)

    def __str__(self):
        return self.dev_id


class GatewayModel(models.Model):
    gtw_network_id = models.CharField(max_length=200)
    latitude = models.IntegerField(default=None)
    longitude = models.IntegerField(default=None)
    altitude = models.IntegerField(default=None)
    location = models.CharField(max_length=200)

    def __str__(self):
        return self.gtw_network_id


class ConnectionModel(models.Model):
    gateway_id = models.ForeignKey(GatewayModel, models.CASCADE, null=False)
    service_id = models.ForeignKey(ServiceModel, models.CASCADE, null=False)
    device_id = models.ForeignKey(DeviceModel, models.CASCADE, null=False)
    rssi = models.IntegerField(default=None)
    snr = models.IntegerField(default=None)
