from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Address

class AddressListView(APIView):
    def get(self, request):
        addresses = Address.objects.values()
        return Response(addresses)
