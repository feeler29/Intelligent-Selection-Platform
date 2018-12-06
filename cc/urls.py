"""cc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView
from django.conf.urls import include
from django.conf.urls.i18n import i18n_patterns
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('enginedata/',include('enginedata.urls')),
    #path('',include('sitedata.urls')),
    #path(r'^i18n/', include('django.conf.urls.i18n')),
 #   path('i18n/', include('django.conf.urls.i18n')),
#home page is redirected to enginedata page, change later
    #path('', RedirectView.as_view(url='/enginedata/', permanent=True)),

]
# urlpatterns += i18n_patterns(
#      path('', include('enginedata.urls')),
#  )

urlpatterns += [
    path('sitedata/',views.SiteDataCreate.as_view(), name='site_data_create'),
    path('sitedata/<int:pk>/update',views.SiteDataUpdate.as_view(), name='site_data_update'),
    path('electricdata/create',views.ElectricDataCreate.as_view(),name='electric_data_create'),
    path('fueldata/create',views.FuelDataCreate.as_view(),name='fuel_data_create'),
    path('thermaldata/create',views.ThermalDataCreate.as_view(),name='thermal_data_create'),
]