from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'clients', views.ClientViewSet)
router.register(r'houses', views.HouseViewSet)
router.register(r'unities', views.UnityOfConsumptionViewSet)
router.register(r'solar-systems', views.SolarEnergySystemViewSet)



urlpatterns = [
    path('api/', include(router.urls)),
]