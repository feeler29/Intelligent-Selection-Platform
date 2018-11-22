from django.db import models

from django.urls import reverse

from django.utils.translation import gettext_lazy as _

class ModuleVersion(models.Model):
	
	version = models.OneToOneField(
		'Technicaldata',
		on_delete=models.CASCADE,
		help_text=_('Module version number'),
	)

	manufacturer = models.ForeignKey(
		'Manufacturer',
		on_delete=models.SET_NULL,
		null=True
	)


	Electric_frequency = (
		(50,'50Hz'),
		(60,'60Hz'),
	)

	frequency = models.IntegerField(
		choices=Electric_frequency,
		default=50,
	)


	gas_type = models.ForeignKey(
		'Genre',
		on_delete=models.SET_NULL,
		null=True
	)

	
	NOx_emission = (
		('ultralow','<50mg/m3'),
		('low','<250mg/m3'),
		('middle','<500mg/m3'),
		('high','>500mg/m3'),
	)

	NOx = models.CharField(
		max_length=100,
		choices=NOx_emission,
		default=_('middle')
	)


	class Meta:
		ordering = ['gas_type__name','version__electrical_output']

	def __str__(self):

		return f'{self.version.name}_{self.version.electrical_output}kW_{self.gas_type}_{self.version.NOx_emission}mg'


	def get_absolute_url(self):

		return reverse('module-detail',args=[str(self.id)])



class Technicaldata(models.Model):

	name = models.CharField(
		max_length=100,
	)

	energy_input = models.IntegerField(help_text='kW')

	mechanical_output = models.IntegerField(help_text='kW')

	electrical_output = models.IntegerField(help_text='kW')

	thermal_output = models.IntegerField(help_text='kW')

	electrical_efficiency = models.FloatField(help_text='%')

	thermal_efficiency = models.FloatField(help_text='%')

	total_efficiency = models.FloatField(help_text='%')

	NOx_emission = models.IntegerField(help_text='mg/m3')

	ICWT = models.IntegerField(help_text=_('°C intercooler water temperature'))

	CR = models.FloatField(help_text=_('compression ratio'))

	engine_speed = models.IntegerField(help_text='rpm')

	
	# GASTYPE = (
	# 	('NG','Natural gas'),
	# 	('BG','Biogas'),
	# 	('SG','Sewage gas'),
	# 	('LG','Landfill gas'),
	# 	('APG','Flaregas'),
	# 	('CG','Coalmine gas'),
	# 	('HD','HD-5 Propane'),
	# )
	fuel_gas_type = models.ForeignKey(
		'Genre',
		on_delete=models.SET_NULL,
		null=True,
	)

	# fuel_gas_type = models.CharField(
	# 	max_length=100,
	# 	choices=GASTYPE,
	# 	default='NG'
	# 	)

	class Meta:
		ordering = ['fuel_gas_type','electrical_output']

	def __str__(self):

		return f'{self.name}_{self.electrical_output}kW_{self.fuel_gas_type}'

	def get_absolute_url(self):

		return reverse('ts-detail',args=[str(self.id)])




class Manufacturer(models.Model):

	MANU = (
    	('Jenbacher','Jenbacher'),
    	('Waukesha','Waukesha'),
    	('Siemens','Siemens'),
    	('Solar','Solar'),
    )

	name = models.CharField(
		max_length=100,
		choices=MANU,
		blank=True,
		default='Jenbacher'
		)
    	

	def __str__(self):

		return self.name



class Genre(models.Model):

	GASTYPE = (
		('Natural gas','Natural gas'),
		('Biogas','Biogas'),
		('Sewage gas','Sewage gas'),
		('Landfill gas','Landfill gas'),
		('Flaregas','Flaregas'),
		('Coalmine gas','Coalmine gas'),
		('HD-5 Propane','HD-5 Propane'),
	)

	name = models.CharField(
		max_length=100,
		choices=GASTYPE,
		blank=True,
		default='Natural gas'
		)

	def __str__(self):

		return self.name


