from django.shortcuts import render,get_object_or_404

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.urls import reverse_lazy

from sitedata.models import SiteData

import numpy as np

from bokeh.plotting import figure,output_file,show

from bokeh.embed import components

from django.utils.translation import gettext_lazy as _

from scipy import interpolate as ipl

class SiteDataCreate(CreateView):
    model = SiteData
    fields = '__all__'

class SiteDataUpdate(UpdateView):
    model = SiteData
    fields = '__all__'


#根据功率段选择燃气内燃机

def engineselection(power):

    engine=['J312','J316','J320','J420','J612','J620','J624']

    if power<350:
        genset=_('not applicable')
        number=0

    elif power in range(350,650):
        genset=engine[0]
        number=1

    elif power in range(650,850):
        genset=engine[1]
        number=1

    elif power in range(850,1100):
        genset=engine[2]
        number=1

    elif power in range(1100,1500):
        genset=engine[3]
        number=1

    elif power in range(1500,2000):
        genset=engine[4]
        number=1

    elif power in range(2000,3000):
        genset=engine[3]
        number=2

    elif power in range(3000,3400):
        genset=engine[5]
        number=1

    elif power in range(3400,4500):
        genset=engine[3]
        number=3

    else:
        genset=engine[5]
        number=int(power/3300)


    return (genset,number)


#根据功率段选择燃气轮机

def turbineselection(power): 

    turbine=['KB5S','KB7S']

    if power in range(3500,4000):
        genset=turbine[0]
        number=1

    elif power in range(4000,5400):
        genset=turbine[1]
        number=1

    elif power in range(5400,8000):
        genset=turbine[0]
        number=2

    elif power in range(8000,11000):
        genset=turbine[1]
        number=2

    else:
        genset=turbine[1]
        number=int(power/5400)

    return (genset,number)



def Result(request,pk):

    site = get_object_or_404(SiteData,pk=pk)
    power1=[site.ave_elec_demand_Jan,
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

    month=[i for i in range(1,13)]

#根据并网模式选择电功率

    if site.grid_mode==1:
        power=np.average(power1)

    else:
        power=np.max(power1)

#根据余热利用类型选择设备类型

    if site.majorload=='hot water':
        
        result=engineselection(power)

    elif site.majorload=='both water and steam':
        
        result=engineselection(power)

    elif site.majorload=='process steam':
 
        if power<4000:
            result=engineselection(power)

        else:
            result=turbineselection(power)

#绘制月用电功率图
    x_month=np.linspace(1,12,100)
    y_power=ipl.pchip_interpolate(month,power1,x_month)
    plot1 = figure(title='月平均用电功率', 
        x_axis_label='时间(月)', 
        y_axis_label='功率(kW)', 
        plot_width =600,
        plot_height =400)
    plot1.line(x_month, y_power, line_width = 2)
    script1,div1 = components(plot1)

#传递参数到模板
    context = {
    'site':site,
    'genset':result[0],
    'number':result[1],
    'script1':script1,
    'div1':div1,
    }

    return render(request,'result.html',context)


