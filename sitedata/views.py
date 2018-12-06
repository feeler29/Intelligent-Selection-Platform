from django.shortcuts import render,get_object_or_404

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

from sitedata.models import SiteData

class SiteDataCreate(CreateView):
	model = SiteData
	fields = '__all__'

class SiteDataUpdate(UpdateView):
	model = SiteData
	fields = '__all__'


# class ElectricDataCreate(CreateView):
# 	model = ElectricUseData
# 	fields = '__all__'
# 	success_url = reverse_lazy('fuel_data_create')

# class FuelDataCreate(CreateView):
# 	model = FuelUseData
# 	fields = '__all__'
# 	success_url = reverse_lazy('thermal_data_create')

# class ThermalDataCreate(CreateView):
# 	model = ThermalLoads
# 	fields = '__all__'
# 	success_url = reverse_lazy('thermal_data_update')

# class ThermalDataUpdate(UpdateView):
# 	model = ThermalLoads
# 	fields = '__all__'
# 	#success_url = reverse_lazy('result')


def Result(request,pk):

	site = get_object_or_404(SiteData,pk=pk)
	power=site.ave_elec_demand_Jan

	if site.grid_mode==1: #并网不上网
       if power<500:
       	model='J320'

	context = {
	'site':site,
	'model':model,
	}

	return render(request,'result.html',context)


