# Generated by Django 4.2.11 on 2025-04-18 01:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0008_alter_doctors_available_days'),
        ('reservation', '0016_alter_booking_doctor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='appointment', to='doctors.doctors', blank=True, null=True),
        ),
    ]
