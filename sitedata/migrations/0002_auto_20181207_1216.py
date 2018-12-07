# Generated by Django 2.1.2 on 2018-12-07 04:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sitedata', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='electricusedata',
            name='projectname',
        ),
        migrations.DeleteModel(
            name='FuelUseData',
        ),
        migrations.DeleteModel(
            name='ThermalLoads',
        ),
        migrations.AddField(
            model_name='sitedata',
            name='ave_elec_demand_Apr',
            field=models.FloatField(default=1, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Average electric demand April (kW)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sitedata',
            name='ave_elec_demand_Aug',
            field=models.FloatField(default=1, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Average electric demand August (kW)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sitedata',
            name='ave_elec_demand_Dec',
            field=models.FloatField(default=1, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Average electric demand December (kW)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sitedata',
            name='ave_elec_demand_Feb',
            field=models.FloatField(default=1, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Average electric demand February (kW)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sitedata',
            name='ave_elec_demand_Jan',
            field=models.FloatField(default=1, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Average electric demand January (kW)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sitedata',
            name='ave_elec_demand_Jul',
            field=models.FloatField(default=1, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Average electric demand July (kW)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sitedata',
            name='ave_elec_demand_Jun',
            field=models.FloatField(default=1, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Average electric demand June (kW)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sitedata',
            name='ave_elec_demand_Mar',
            field=models.FloatField(default=1, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Average electric demand March (kW)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sitedata',
            name='ave_elec_demand_May',
            field=models.FloatField(default=1, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Average electric demand May (kW)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sitedata',
            name='ave_elec_demand_Nov',
            field=models.FloatField(default=1, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Average electric demand November (kW)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sitedata',
            name='ave_elec_demand_Otc',
            field=models.FloatField(default=1, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Average electric demand October (kW)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sitedata',
            name='ave_elec_demand_Sep',
            field=models.FloatField(default=1, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Average electric demand September (kW)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sitedata',
            name='elec_consum',
            field=models.FloatField(default=1, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Electric consumption (kWh)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sitedata',
            name='grid_mode',
            field=models.BooleanField(default=1, verbose_name='grid parallel without power injecting'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sitedata',
            name='majorload',
            field=models.CharField(blank=True, choices=[('hot water', 'hot water'), ('process steam', 'process steam'), ('sterilization', 'sterilization'), ('space heating', 'space heating')], max_length=100),
        ),
        migrations.AddField(
            model_name='sitedata',
            name='peak_elec_demand_Jan',
            field=models.FloatField(default=1, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Peak electric demand January (kW)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sitedata',
            name='primaryfuel',
            field=models.CharField(blank=True, choices=[('natural gas', 'natural gas'), ('coal', 'coal'), ('oil', 'oil')], max_length=100),
        ),
        migrations.AddField(
            model_name='sitedata',
            name='service_voltage',
            field=models.FloatField(default=1, validators=[django.core.validators.MaxValueValidator(40), django.core.validators.MinValueValidator(0)], verbose_name='Service voltage (kV)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sitedata',
            name='steam_press',
            field=models.FloatField(default=1, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Required Steam Pressure'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sitedata',
            name='steam_temp',
            field=models.FloatField(default=1, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Required Steam Temperature'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sitedata',
            name='steamdemand_ave',
            field=models.FloatField(default=1, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Average Steam Demand'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sitedata',
            name='steamdemand_max',
            field=models.FloatField(default=1, validators=[django.core.validators.MinValueValidator(0)], verbose_name='Maximum Steam Demand (t/h)'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sitedata',
            name='track',
            field=models.BooleanField(default=False, help_text='do themal loads generally track electric loads', verbose_name='Track'),
        ),
        migrations.AlterField(
            model_name='sitedata',
            name='alitude',
            field=models.IntegerField(default=900, validators=[django.core.validators.MaxValueValidator(5000), django.core.validators.MinValueValidator(0)], verbose_name='Alitude (m)'),
        ),
        migrations.AlterField(
            model_name='sitedata',
            name='operating_days',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(7), django.core.validators.MinValueValidator(0)], verbose_name='Operating days per week'),
        ),
        migrations.AlterField(
            model_name='sitedata',
            name='operating_hours',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(24), django.core.validators.MinValueValidator(0)], verbose_name='Operating hours per day'),
        ),
        migrations.AlterField(
            model_name='sitedata',
            name='operating_weeks',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(54), django.core.validators.MinValueValidator(0)], verbose_name='Operating weeks per year'),
        ),
        migrations.AlterField(
            model_name='sitedata',
            name='summer_temp',
            field=models.FloatField(default=30, validators=[django.core.validators.MaxValueValidator(50), django.core.validators.MinValueValidator(0)], verbose_name='Summer design temperature'),
        ),
        migrations.AlterField(
            model_name='sitedata',
            name='winter_temp',
            field=models.FloatField(default=-10, validators=[django.core.validators.MaxValueValidator(50), django.core.validators.MinValueValidator(-50)], verbose_name='Winter design temperature'),
        ),
        migrations.DeleteModel(
            name='ElectricUseData',
        ),
    ]
