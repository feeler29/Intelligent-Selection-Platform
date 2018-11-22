from django.db import models

from django.urls import reverse

from django.utils.translation import gettext_lazy as _


class SiteData(models.Model):

	projectname = models.CharField(
		max_length=200,
		verbose_name=_('Project name'),
		)

	operating_hours = models.IntegerField(
		verbose_name=_('Operating hours per day')
		)

	operating_days = models.IntegerField(
		verbose_name=_('Operating days per week')
		)

	operating_weeks = models.IntegerField(
		verbose_name=_('Operating weeks per year')
		)

	alitude = models.IntegerField(
		verbose_name=_('Alitude (m)')
		)

	summer_temp = models.FloatField(
		verbose_name=_('Summer design temperature')
		)

	winter_temp = models.FloatField(
		verbose_name=_('Winter design temperature')
		)


	def __str__(self):

		return self.projectname


class ElectricUseData(models.Model):

	projectname = models.ForeignKey(
		'SiteData',
		on_delete=models.CASCADE,
		)

	grid_parallel = models.BooleanField(
		verbose_name=_('grid parallel without power injecting')
		)

	service_voltage = models.FloatField(
		verbose_name=_('Service voltage (kV)')
		)

	Ave_Elec_Demand_Jan = models.FloatField(
		verbose_name=_('Average electric demand January (kW)')
		)

	Peak_Elec_Demand_Jan = models.FloatField(
		verbose_name=_('Peak electric demand January (kW)')
		)
    
    # Elec_Consum = models.FloatField(
    # 	verbose_name=_('Electric consumption (kWh)')
    # 	)
    # def __str__(self):

    # 	return self.projectname


class FuelUseData(models.Model):
    pass


class ThermalLoads(models.Model):

	pass
