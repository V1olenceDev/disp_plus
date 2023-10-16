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
    approved_vehicle = serializers.PrimaryKeyRelatedField(
        queryset=Transport.objects.filter(status=True),
        many=False, required=False)

    creator = CustomUserSerializer(read_only=True)
    approved_vehicle = TransportSerializer(read_only=True)
    assigned_driver = CustomUserSerializer(read_only=True)
    approved_vehicle_id = serializers.IntegerField(
        write_only=True, required=False)
    assigned_driver = serializers.PrimaryKeyRelatedField(
        queryset=CustomUser.objects.filter(role='Водитель'),
        many=False, required=False)

    def update(self, instance, validated_data):
        approved_vehicle_id = validated_data.pop('approved_vehicle_id', None)
        assigned_driver_id = validated_data.pop('assigned_driver_id', None)

        if approved_vehicle_id:
            instance.approved_vehicle = Transport.objects.get(
                id=approved_vehicle_id)
        if assigned_driver_id:
            instance.assigned_driver = CustomUser.objects.get(
                id=assigned_driver_id)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

    creator = CustomUserSerializer()
    requested_vehicle = TransportSerializer()
    approved_vehicle = TransportSerializer()
    assigned_driver = CustomUserSerializer()

    class Meta:
        model = Order
        fields = '__all__'
