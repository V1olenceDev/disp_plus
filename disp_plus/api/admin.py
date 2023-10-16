from django.contrib import admin
from .models import CustomUser, Transport, Order

admin.site.register(CustomUser)
admin.site.register(Transport)
admin.site.register(Order)
