# Generated by Django 4.1.4 on 2023-02-02 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managment', '0006_profiles_hr_profiles_manager_hr_employe'),
    ]

    operations = [
        migrations.AddField(
            model_name='leave_manag',
            name='hr_approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='leave_manag',
            name='hr_reject',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='leave_manag',
            name='manager_approve',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='leave_manag',
            name='manager_reject',
            field=models.BooleanField(default=False),
        ),
    ]
