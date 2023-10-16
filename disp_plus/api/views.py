from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .permissions import IsCustomer, IsDispatcher, IsChief, IsDriver

from .models import CustomUser, Transport, Order
from .serializers import (
    CustomUserSerializer,
    TransportSerializer,
    OrderSerializer
)


class CustomUserList(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class CustomUserDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class TransportList(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Transport.objects.all()
    serializer_class = TransportSerializer


class TransportDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Transport.objects.all()
    serializer_class = TransportSerializer


class OrderList(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class MyOrders(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.filter(creator=self.request.user)


class OrdersInProgress(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    permission_classes = [IsCustomer]
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.filter(
            creator=self.request.user, status='Принята')


class DispatcherOrdersToReview(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    permission_classes = [IsDispatcher]
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.filter(status='Не рассмотрена')


class DispatcherOrderHistory(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    permission_classes = [IsDispatcher]
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.filter(
            status__in=['Отклонена', 'На рассмотрении'])


class ChiefOrdersToReview(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.filter(status='На рассмотрении')

    def put(self, request, *args, **kwargs):
        order_id = request.data.get('order_id')
        order = get_object_or_404(Order, id=order_id)
        serializer = self.get_serializer(
            order, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class ChiefOrderHistory(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    permission_classes = [IsChief]
    serializer_class = OrderSerializer

    def get_queryset(self):
        return Order.objects.filter(status__in=['Отклонена', 'Принята'])


class DriverSchedule(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    permission_classes = [IsDriver]
    serializer_class = OrderSerializer

    def get_queryset(self):
        date_filter = self.request.query_params.get('date', None)
        queryset = Order.objects.filter(assigned_driver=self.request.user)
        if date_filter:
            queryset = queryset.filter(date=date_filter)
        return queryset


class ManageVehicles(generics.ListAPIView, generics.UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Transport.objects.all()
    serializer_class = TransportSerializer
    permission_classes = [IsChief]

    def get_queryset(self):
        return Transport.objects.all()

    def perform_update(self, serializer):
        serializer.save()
