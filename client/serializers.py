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


class EnergySupplierSerializer(serializers.ModelSerializer):
    address = serializers.CharField(source='house.address')

    class Meta:
        model = UnityOfConsumption
        fields = ('id', 'address', 'is_generator', 'is_beneficiary')


class UnityOfConsumptionSerializer(serializers.ModelSerializer):
    bill_amount = serializers.SerializerMethodField()
    supplier_addresses = serializers.SerializerMethodField()
    energy_suppliers_info = EnergySupplierSerializer(
        many=True,
        read_only=True,
        source='energy_suppliers'
    )

    class Meta:
        model = UnityOfConsumption
        # Specify the fields you want to include explicitly to avoid including 'energy_suppliers'
        fields = (
            'id',
            'house',
            'energy_consumed',
            'energy_generated',
            'energy_credit',
            'energy_rate',
            'is_generator',
            'is_beneficiary',
            'bill_amount',
            'supplier_addresses',
            'energy_suppliers_info'
        )

    def get_bill_amount(self, obj):
        return obj.calculate_bill()

    def get_supplier_addresses(self, obj):
        return obj.get_energy_supplier_addresses()


class SolarEnergySystemSerializer(serializers.ModelSerializer):
    class Meta:
        model = SolarEnergySystem
        fields = '__all__'
