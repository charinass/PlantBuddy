from django.contrib import admin
from PlantBuddy.models import DeviceModel, ServiceModel, GatewayModel, ConnectionModel


# Register your models here.
admin.site.register(DeviceModel)
admin.site.register(ServiceModel)
admin.site.register(GatewayModel)
admin.site.register(ConnectionModel)