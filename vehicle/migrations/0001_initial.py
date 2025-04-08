# Generated by Django 5.2 on 2025-04-08 16:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('driver', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model', models.CharField(max_length=50)),
                ('vehicle_plate', models.CharField(max_length=7)),
                ('checkin_datetime', models.DateTimeField(auto_now=True)),
                ('parked', models.BooleanField(default=False)),
                ('driver', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, to='driver.driver')),
            ],
        ),
    ]
