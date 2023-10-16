from rest_framework import serializers

from .models import CustomUser, Transport, Order


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = (
            'id',
            'first_name',
            'last_name',
            'role',
            'department',
            'phone_num'
            )


class TransportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transport
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):
    creator = CustomUserSerializer()
    requested_vehicle = TransportSerializer()
    approved_vehicle = TransportSerializer()
    assigned_driver = CustomUserSerializer()

    class Meta:
        model = Order
        fields = '__all__'
