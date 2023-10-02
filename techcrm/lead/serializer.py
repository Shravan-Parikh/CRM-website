from django.urls import path, include

from lead.models import Lead

from rest_framework import serializers

class leadSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Lead
        fields = '__all__'