from django.db import models

class Address(models.Model):
    address_line1 = models.CharField(max_length=255)
    address_line2 = models.CharField(max_length=255, blank=True, null=True)
    district = models.CharField(max_length=100, blank=True, null=True)
    city = models.CharField(max_length=100)
    departement = models.CharField(max_length=100, blank=True, null=True,choices=[('Ouest','ouest'),('Sud','sud'),('Nord','nord'),('Nord-Est','nord-est'),('Nord-Ouest','nord-ouest'),('Centre','centre'),('Sud-Est','sud-est'),('Artibonite','artibonite'),('Grande-Anse','grande-anse'),('Nippes','nippes')])
    postal_code = models.CharField(max_length=20, blank=True, null=True)
    country = models.CharField(max_length=100, default="Haïti")
    type = models.CharField(max_length=50, choices=[('residential', 'Residential'), ('commercial', 'Commercial')], blank=True, null=True)

    def __str__(self):
        return f"{self.address_line1}, {self.city}"

