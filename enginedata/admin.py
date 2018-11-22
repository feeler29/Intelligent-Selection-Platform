
from django.contrib import admin

from enginedata.models import ModuleVersion,Technicaldata,Manufacturer,Genre

class TechnicaldataAdmin(admin.ModelAdmin):
	list_display = ('name','electrical_output','fuel_gas_type',)
	list_filter = ('fuel_gas_type','NOx_emission')

admin.site.register(ModuleVersion)
admin.site.register(Technicaldata,TechnicaldataAdmin)
admin.site.register(Manufacturer)
admin.site.register(Genre)
