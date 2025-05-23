# Generated by Django 4.2.11 on 2025-03-12 19:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0010_remove_booking_appointment_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='age',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='appointment_date',
            field=models.DateField(blank=True, default=datetime.date.today, null=True),
        ),
        migrations.AddField(
            model_name='booking',
            name='appointment_time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]
