# Generated by Django 2.0.5 on 2018-11-15 02:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enginedata', '0006_technicaldata_fuel_gas_type'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='technicaldata',
            options={'ordering': ['fuel_gas_type', 'electrical_output']},
        ),
    ]