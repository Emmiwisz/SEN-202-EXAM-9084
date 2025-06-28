from rest_framework import serializers
from .models import Manager, Intern, Address

class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        exclude = ['has_company_card'] 

class InternSerializer(serializers.ModelSerializer):
    class Meta:
        model = Intern
        fields = '__all__'

class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'
