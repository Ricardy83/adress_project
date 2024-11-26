from django.contrib import admin
from .models import Address

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('address_line1', 'city', 'departement', 'country', 'type')
    search_fields = ('address_line1', 'city', 'departement', 'postal_code')

