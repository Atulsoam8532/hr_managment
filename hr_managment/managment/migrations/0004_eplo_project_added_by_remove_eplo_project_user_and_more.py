# Generated by Django 4.1.4 on 2023-02-02 05:56

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('managment', '0003_leave_manag_eplo_project'),
    ]

    operations = [
        migrations.AddField(
            model_name='eplo_project',
            name='added_by',
            field=models.CharField(default='nothing', max_length=20),
        ),
        migrations.RemoveField(
            model_name='eplo_project',
            name='user',
        ),
        migrations.AddField(
            model_name='eplo_project',
            name='user',
            field=models.ManyToManyField(related_name='us', to=settings.AUTH_USER_MODEL),
        ),
    ]
