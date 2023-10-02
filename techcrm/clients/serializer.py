from django.urls import path, include

from .models import Client

from rest_framework import serializers

class ClientSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Client
        fields = '__all__'