# Generated by Django 5.1.3 on 2024-11-24 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('addresses', '0003_rename_region_address_departement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='departement',
            field=models.CharField(blank=True, choices=[('Ouest', 'ouest'), ('Sud', 'sud')], max_length=100, null=True),
        ),
    ]
