from django.urls import path
from . import views


urlpatterns = [
    path('sitedata/',views.SiteDataCreate.as_view(), name='site_data_create'),
    path('sitedata/<int:pk>/update',views.SiteDataUpdate.as_view, name='site_data_update'),
    path('electricdata/create',views.ElectricDataCreate.as_view(),name='electric_data_create'),
    path('fueldata/create',views.FuelDataCreate.as_view(),name='fuel_data_create'),
    path('thermaldata/create',views.ThermalDataCreate.as_view(),name='thermal_data_create'),
]