# Generated by Django 4.2.11 on 2025-04-17 05:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0008_alter_doctors_available_days'),
        ('reservation', '0014_booking_age_booking_appointment_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='booking',
            name='doctor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='appointment', to='doctors.doctors'),
        ),
    ]
