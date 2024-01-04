from rest_framework import viewsets
from rest_framework.decorators import action
from .models import Client, House, UnityOfConsumption, SolarEnergySystem
from .serializers import ClientSerializer, HouseSerializer, UnityOfConsumptionSerializer, SolarEnergySystemSerializer
from rest_framework.response import Response



class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer


class HouseViewSet(viewsets.ModelViewSet):
    queryset = House.objects.all()
    serializer_class = HouseSerializer


class UnityOfConsumptionViewSet(viewsets.ModelViewSet):
    queryset = UnityOfConsumption.objects.all()
    serializer_class = UnityOfConsumptionSerializer

    @action(detail=True, methods=['get'])
    def bill(self, request, pk=None):
        uc = self.get_object()
        bill_amount = uc.calculate_bill()
        return Response({'bill_amount': bill_amount})


class SolarEnergySystemViewSet(viewsets.ModelViewSet):
    queryset = SolarEnergySystem.objects.all()
    serializer_class = SolarEnergySystemSerializer
