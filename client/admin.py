from django.contrib import admin
from .models import Client, House, UnityOfConsumption, SolarEnergySystem

admin.site.register(Client)
admin.site.register(House)
admin.site.register(UnityOfConsumption)
admin.site.register(SolarEnergySystem)