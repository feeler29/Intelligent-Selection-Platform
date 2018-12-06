from django.forms import ModelForm

from sitedata.models import SiteData,ElectricUseData,FuelUseData,ThermalLoads

class SiteDataForm(ModelForm):

    class Meta:
        model = SiteData
        fields = '__all__'


class ElectricDataForm(ModelForm):

    class Meta:
        model = ElectricUseData
        fields = '__all__'


class FuelDataForm(ModelForm):

	class Meta:
		model = FuelUseData
		fields = '__all__'


class ThermalDataForm(ModelForm):

	class Meta:
		model = ThermalLoads
		fields = '__all__'