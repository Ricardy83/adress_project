# Generated by Django 5.1.3 on 2024-11-23 06:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0002_remove_address_latitude_remove_address_longitude_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='region',
            new_name='departement',
        ),
    ]
