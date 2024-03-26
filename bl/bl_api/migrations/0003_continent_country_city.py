# Generated by Django 5.0.1 on 2024-03-26 17:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bl_api', '0002_place_delete_todo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Continent',
            fields=[
                ('continent_code', models.TextField(primary_key=True, serialize=False)),
                ('continent_name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('country_code', models.TextField(primary_key=True, serialize=False)),
                ('country_name', models.TextField()),
                ('capital', models.TextField()),
                ('continent_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bl_api.continent')),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('geoname_id', models.IntegerField(primary_key=True, serialize=False)),
                ('city_name', models.TextField()),
                ('alternate_names', models.TextField()),
                ('country_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bl_api.country')),
            ],
        ),
    ]