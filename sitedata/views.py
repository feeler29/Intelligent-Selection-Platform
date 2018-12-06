from django.shortcuts import render

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

from sitedata.models import SiteData,ElectricUseData,FuelUseData,ThermalLoads

class SiteDataCreat(CreatView):
	model = SiteData
	fields = '__all__'
	success_url = reverse_lazy('electric_data_creat')

class SiteDataUpdate(UpdateView):
	model = SiteData
	fields = '__all__'

class ElectricDataCreat(CreatView):
	model = ElectricUseData
	fields = '__all__'
	success_url = reverse_lazy('fuel_data_creat')

class FuelDataCreat(CreatView):
	model = FuelUseData
	fields = '__all__'
	success_url = reverse_lazy('thermal_data_creat')

class ThermalDataCreat(CreatView):
	model = ThermalLoads
	fields = '__all__'
	success_url = reverse_lazy('result')