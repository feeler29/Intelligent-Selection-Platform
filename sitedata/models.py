from django.db import models

from django.urls import reverse

from django.utils.translation import gettext_lazy as _


class SiteData(models.Model):

# site information 

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
		verbose_name=_('Alitude (m)'),
		default=900,
		)

	summer_temp = models.FloatField(
		verbose_name=_('Summer design temperature'),
		default=30,
		)

	winter_temp = models.FloatField(
		verbose_name=_('Winter design temperature'),
		default=-10,
		)


# electric use data

	grid_mode = models.BooleanField(
		verbose_name=_('grid parallel without power injecting')
		)

	service_voltage = models.FloatField(
		verbose_name=_('Service voltage (kV)')
		)

	ave_elec_demand_Jan = models.FloatField(
		verbose_name=_('Average electric demand January (kW)')
		)

	peak_dlec_demand_Jan = models.FloatField(
		verbose_name=_('Peak electric demand January (kW)')
		)

	elec_consum = models.FloatField(
	    verbose_name=_('Electric consumption (kWh)')
	    )


# fuel use data

	fuel_type = (
		('natural gas',_('natural gas')),
		('coal',_('coal')),
		('oil',_('oil')),
		)

	primaryfuel = models.CharField(
		max_length=100,
		choices=fuel_type,
		blank=True,
		)


# thermal loads

	load_type=(
		('hot water',_('hot water')),
		('process steam',_('process steam')),
		('sterilization',_('sterilization')),
		('space heating',_('space heating')),
		)
 
	majorload = models.CharField(
		max_length=100,
		choices=load_type,
		blank=True,
		)

	steamdemand_max = models.FloatField(
		verbose_name=_('Maximum Steam Demand (t/h)')

		)

	steamdemand_ave = models.FloatField(
		verbose_name=_('Average Steam Demand')
		)

	steam_temp = models.FloatField(
		verbose_name=_('Required Steam Temperature')
		)

	steam_press = models.FloatField(
		verbose_name=_('Required Steam Pressure')
		)

	track = models.BooleanField(
		verbose_name=_('Track'),
		help_text=_('do themal loads generally track electric loads'),
		default=False
		)

	# def __str__(self):

	# 	return self.projectname
	def get_absolute_url(self):
		return reverse('result',kwargs={'pk':self.pk})

class Result(models.Model):
	pass