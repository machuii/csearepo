# Generated by Django 4.0.5 on 2023-01-09 02:37

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('playlistsdb', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playlist',
            name='songs',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=100), null=True, size=None),
        ),
    ]