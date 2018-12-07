from django.shortcuts import render,get_object_or_404

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

from sitedata.models import SiteData

import numpy as np

class SiteDataCreate(CreateView):
	model = SiteData
	fields = '__all__'

class SiteDataUpdate(UpdateView):
	model = SiteData
	fields = '__all__'


def Result(request,pk):

	site = get_object_or_404(SiteData,pk=pk)
	power=[site.ave_elec_demand_Jan,
	site.ave_elec_demand_Feb,
	site.ave_elec_demand_Mar,
	site.ave_elec_demand_Apr,
	site.ave_elec_demand_May,
	site.ave_elec_demand_Jun,
	site.ave_elec_demand_Jul,
	site.ave_elec_demand_Aug,
	site.ave_elec_demand_Sep,
	site.ave_elec_demand_Oct,
	site.ave_elec_demand_Nov,
	site.ave_elec_demand_Dec,
	]
	model=['J312','J320','J420','J620','J624',]
	
	power_ave=np.average(power)

	num=1
	genset='J320'

	if site.grid_mode==1: #并网不上网
	   if power_ave<1000:
		   genset=model[1]
		   num=1

	context = {
	'site':site,
	'genset':genset,
	'num':num,
	}

	return render(request,'result.html',context)


