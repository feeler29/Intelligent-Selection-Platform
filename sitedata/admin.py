
from django.contrib import admin

from sitedata.models import SiteData

# class TechnicaldataAdmin(admin.ModelAdmin):
# 	list_display = ('name','electrical_output','fuel_gas_type',)
# 	list_filter = ('fuel_gas_type','NOx_emission')


admin.site.register(SiteData)
# admin.site.register(ElectricUseData)
# admin.site.register(FuelUseData)
# admin.site.register(ThermalLoads)