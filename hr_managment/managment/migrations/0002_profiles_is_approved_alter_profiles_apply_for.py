# Generated by Django 4.1.4 on 2023-02-02 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('managment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profiles',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='profiles',
            name='apply_for',
            field=models.CharField(max_length=50),
        ),
    ]
