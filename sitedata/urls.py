from django.urls import path
from . import views


urlpatterns = [
    path('sitedata/creat',views.SiteDataCreat.as_view(), name='site_data_creat'),
    path('sitedata/<int:pk>/update',views.SiteDataUpdate.as_view, name='site_data_update'),
    path('electricdata/creat',views.ElectricDataCreat.as_view(),name='electric_data_creat'),
    path('fueldata/creat',views.FuelDataCreat.as_view(),name='fuel_data_creat'),
    path('thermaldata/creat',views.ThermalDataCreat.as_view(),name='thermal_data_creat'),
]