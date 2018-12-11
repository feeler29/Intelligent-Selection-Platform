from django.db import models

from django.urls import reverse

from django.utils.translation import gettext_lazy as _

from django.core.validators import MaxValueValidator,MinValueValidator


class SiteData(models.Model):

# site information 

	projectname = models.CharField(
		max_length=200,
		verbose_name=_('Project name'),
		)

	operating_hours = models.IntegerField(
		verbose_name=_('Operating hours per day'),
		validators=[MaxValueValidator(24),MinValueValidator(0)]
		)

	operating_days = models.IntegerField(
		verbose_name=_('Operating days per week'),
		validators=[MaxValueValidator(7),MinValueValidator(0)]
		)

	operating_weeks = models.IntegerField(
		verbose_name=_('Operating weeks per year'),
		validators=[MaxValueValidator(54),MinValueValidator(0)]
		)

	alitude = models.IntegerField(
		verbose_name=_('Alitude (m)'),
		default=900,
		validators=[MaxValueValidator(5000),MinValueValidator(0)]
		)

	summer_temp = models.FloatField(
		verbose_name=_('Summer design temperature'),
		default=30,
		validators=[MaxValueValidator(50),MinValueValidator(0)]
		)

	winter_temp = models.FloatField(
		verbose_name=_('Winter design temperature'),
		default=-10,
		validators=[MaxValueValidator(50),MinValueValidator(-50)]
		)


# electric use data

	# mode_type = (
	# 	('1',_('grid parallel without power injecting')),
	# 	('2',_('grid parallel with power injecting')),
	# 	)


	grid_mode = models.BooleanField(
		verbose_name=_('grid parallel without power injection'),
		# choices=mode_type,
		# max_length=100,
		default=1,
		blank=False
		)

	service_voltage = models.FloatField(
		verbose_name=_('Service voltage (kV)'),
		validators=[MaxValueValidator(40),MinValueValidator(0)]
		)

	ave_elec_demand_Jan = models.FloatField(
		verbose_name=_('Average electric demand January (kW)'),
		validators=[MinValueValidator(0)]
		)

	ave_elec_demand_Feb = models.FloatField(
		verbose_name=_('Average electric demand February (kW)'),
		validators=[MinValueValidator(0)]
		)

	ave_elec_demand_Mar = models.FloatField(
		verbose_name=_('Average electric demand March (kW)'),
		validators=[MinValueValidator(0)]
		)

	ave_elec_demand_Apr = models.FloatField(
		verbose_name=_('Average electric demand April (kW)'),
		validators=[MinValueValidator(0)]
		)

	ave_elec_demand_May = models.FloatField(
		verbose_name=_('Average electric demand May (kW)'),
		validators=[MinValueValidator(0)]
		)

	ave_elec_demand_Jun = models.FloatField(
		verbose_name=_('Average electric demand June (kW)'),
		validators=[MinValueValidator(0)]
		)

	ave_elec_demand_Jul = models.FloatField(
		verbose_name=_('Average electric demand July (kW)'),
		validators=[MinValueValidator(0)]
		)

	ave_elec_demand_Aug = models.FloatField(
		verbose_name=_('Average electric demand August (kW)'),
		validators=[MinValueValidator(0)]
		)

	ave_elec_demand_Sep = models.FloatField(
		verbose_name=_('Average electric demand September (kW)'),
		validators=[MinValueValidator(0)]
		)

	ave_elec_demand_Oct = models.FloatField(
		verbose_name=_('Average electric demand October (kW)'),
		validators=[MinValueValidator(0)]
		)

	ave_elec_demand_Nov = models.FloatField(
		verbose_name=_('Average electric demand November (kW)'),
		validators=[MinValueValidator(0)]
		)

	ave_elec_demand_Dec = models.FloatField(
		verbose_name=_('Average electric demand December (kW)'),
		validators=[MinValueValidator(0)]
		)

	peak_elec_demand_Jan = models.FloatField(
		verbose_name=_('Peak electric demand January (kW)'),
		validators=[MinValueValidator(0)]
		)

	elec_consum = models.FloatField(
	    verbose_name=_('Electric consumption (kWh)'),
	    validators=[MinValueValidator(0)]
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
		verbose_name=_('Primary fuel')
		)


# thermal loads

	load_type=(
		('hot water',_('hot water')),
		('process steam',_('process steam')),
		('both water and steam',_('both water and steam')),
		('space heating',_('space heating')),
		)
 
	majorload = models.CharField(
		max_length=100,
		choices=load_type,
		blank=True,
		verbose_name=_('Major loads')
		)

	steamdemand_max = models.FloatField(
		verbose_name=_('Maximum Steam Demand (t/h)'),
		validators=[MinValueValidator(0)]
		)

	steamdemand_ave = models.FloatField(
		verbose_name=_('Average Steam Demand'),
		validators=[MinValueValidator(0)]
		)

	steam_temp = models.FloatField(
		verbose_name=_('Required Steam Temperature'),
		validators=[MinValueValidator(0)]
		)

	steam_press = models.FloatField(
		verbose_name=_('Required Steam Pressure'),
		validators=[MinValueValidator(0)]
		)

	track = models.BooleanField(
		verbose_name=_('Track'),
		help_text=_('do themal loads generally track electric loads'),
		default=False
		)


	def get_absolute_url(self):
		return reverse('result',kwargs={'pk':self.pk})

