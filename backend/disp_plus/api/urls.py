from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
    )

urlpatterns = [
    path('users/', views.CustomUserList.as_view(), name='user-list'),
    path('users/<int:pk>/',
         views.CustomUserDetail.as_view(),
         name='user-detail'),
    path('transports/', views.TransportList.as_view(), name='transport-list'),
    path(
        'transports/<int:pk>/',
        views.TransportDetail.as_view(),
        name='transport-detail'
        ),
    path('orders/', views.OrderList.as_view(), name='order-list'),
    path('orders/<int:pk>/', views.OrderDetail.as_view(), name='order-detail'),
    path('my-orders/',
         views.MyOrders.as_view(),
         name='customer-orders-list'),
    path('orders-in-progress/',
         views.OrdersInProgress.as_view(),
         name='orders-in-progress'),
    path('dispatcher/orders-to-review/',
         views.DispatcherOrdersToReview.as_view(),
         name='dispatcher-orders-to-review'),
    path('dispatcher/order-history/',
         views.DispatcherOrderHistory.as_view(),
         name='dispatcher-order-history'),
    path('chief/orders-to-review/',
         views.ChiefOrdersToReview.as_view(),
         name='chief-orders-to-review'),
    path('chief/order-history/',
         views.ChiefOrderHistory.as_view(),
         name='chief-order-history'),
    path('driver/schedule/',
         views.DriverSchedule.as_view(),
         name='driver-schedule'),
    path('manage-vehicles/',
         views.ManageVehicles.as_view(),
         name='manage-vehicles'),
    path('jwt-token-auth/',
         TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('jwt-token-refresh/',
         TokenRefreshView.as_view(), name='token_refresh'),
]
