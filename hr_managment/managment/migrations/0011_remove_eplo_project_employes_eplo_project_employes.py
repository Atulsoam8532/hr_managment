# Generated by Django 4.1.4 on 2023-02-03 04:54

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('managment', '0010_rename_user_eplo_project_employes'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eplo_project',
            name='employes',
        ),
        migrations.AddField(
            model_name='eplo_project',
            name='employes',
            field=models.ManyToManyField(related_name='us', to=settings.AUTH_USER_MODEL),
        ),
    ]
