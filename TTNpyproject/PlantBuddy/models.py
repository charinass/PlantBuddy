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
    dev_id = models.ForeignKey(DeviceModel, null=False)

    def __str__(self):
        return self.dev_id



