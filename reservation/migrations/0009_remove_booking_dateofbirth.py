# Generated by Django 4.2.11 on 2025-03-12 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0008_remove_booking_appointment_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='dateOfBirth',
        ),
    ]
