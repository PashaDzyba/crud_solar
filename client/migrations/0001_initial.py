# Generated by Django 5.0.1 on 2024-01-04 22:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='House',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=200)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='houses', to='client.client')),
            ],
        ),
        migrations.CreateModel(
            name='UnityOfConsumption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('energy_consumed', models.FloatField(default=0)),
                ('energy_generated', models.FloatField(default=0)),
                ('energy_credit', models.FloatField(default=0)),
                ('energy_rate', models.FloatField(default=0.1)),
                ('house', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='unities', to='client.house')),
            ],
        ),
        migrations.CreateModel(
            name='SolarEnergySystem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('production', models.FloatField()),
                ('uc', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='solar_system', to='client.unityofconsumption')),
            ],
        ),
    ]
