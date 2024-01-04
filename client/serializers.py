from rest_framework import serializers
from .models import Client, House, UnityOfConsumption, SolarEnergySystem

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'

class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = '__all__'


class UnityOfConsumptionSerializer(serializers.ModelSerializer):
    bill_amount = serializers.SerializerMethodField()

    class Meta:
        model = UnityOfConsumption
        fields = '__all__'

    def get_bill_amount(self, obj):
        return obj.calculate_bill()

class SolarEnergySystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolarEnergySystem
        fields = '__all__'

