from django.urls import path
from .views import (
    CustomUserList,
    CustomUserDetail,
    TransportList,
    TransportDetail,
    OrderList,
    OrderDetail
    )

urlpatterns = [
    path('users/', CustomUserList.as_view(), name='user-list'),
    path('users/<int:pk>/', CustomUserDetail.as_view(), name='user-detail'),

    path('transports/', TransportList.as_view(), name='transport-list'),
    path(
        'transports/<int:pk>/',
        TransportDetail.as_view(),
        name='transport-detail'
        ),

    path('orders/', OrderList.as_view(), name='order-list'),
    path('orders/<int:pk>/', OrderDetail.as_view(), name='order-detail'),
]
