# Generated by Django 4.2.6 on 2023-11-19 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('measurement', '0007_alter_measurement_sensor'),
    ]

    operations = [
        migrations.AddField(
            model_name='measurement',
            name='photo',
            field=models.ImageField(null=True, upload_to='photo/'),
        ),
    ]
