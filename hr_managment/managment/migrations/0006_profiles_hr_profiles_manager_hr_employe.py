# Generated by Django 4.1.4 on 2023-02-02 06:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('managment', '0005_alter_eplo_project_rm'),
    ]

    operations = [
        migrations.AddField(
            model_name='profiles',
            name='HR',
            field=models.CharField(default='nothing', max_length=10),
        ),
        migrations.AddField(
            model_name='profiles',
            name='manager',
            field=models.CharField(default='nothing', max_length=10),
        ),
        migrations.CreateModel(
            name='Hr_employe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empolye', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
