from django.shortcuts import render,get_object_or_404

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

from sitedata.models import SiteData

class SiteDataCreate(CreateView):
	model = SiteData
	fields = '__all__'
	success_url = reverse_lazy('site_data_update')

class SiteDataUpdate(UpdateView):
	model = SiteData
	fields = '__all__'
	def get_absolute_url(self):
		return reverse('result',kwargs={'pk':self.pk})

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
	context = {
	'site':site,
	}

	return render(request,'result.html',context)


