# Generated by Django 4.2.6 on 2023-11-19 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0002_rename_id_sensor_measurement_sensor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='measurement',
            name='temperature',
            field=models.FloatField(),
        ),
    ]
