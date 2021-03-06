# Generated by Django 3.1.7 on 2022-02-02 12:32

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facility_name', models.CharField(max_length=100, verbose_name='Hospital Name')),
                ('facility_type', models.CharField(max_length=100, verbose_name='Hospital Type')),
                ('ward', models.CharField(max_length=100, verbose_name='Ward')),
                ('ownership', models.CharField(max_length=100, verbose_name='Ownership')),
                ('lga', models.CharField(max_length=100, verbose_name='L.G.A')),
                ('lon', models.FloatField(verbose_name='Longitude')),
                ('lat', models.FloatField(verbose_name='Latitude')),
                ('geom', django.contrib.gis.db.models.fields.PointField(srid=4326)),
            ],
        ),
    ]
