from rest_framework import generics
from .models import CustomUser, Transport, Order
from .serializers import (CustomUserSerializer,
                          TransportSerializer,
                          OrderSerializer
                          )


# Представления для CustomUser
class CustomUserList(generics.ListCreateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class CustomUserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


# Представления для Transport
class TransportList(generics.ListCreateAPIView):
    queryset = Transport.objects.all()
    serializer_class = TransportSerializer


class TransportDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Transport.objects.all()
    serializer_class = TransportSerializer


# Представления для Order
class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
