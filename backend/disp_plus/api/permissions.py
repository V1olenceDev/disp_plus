from rest_framework import permissions


class IsCustomer(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.role == 'Заказчик'

    def has_object_permission(self, request, view, obj):
        return obj.creator == request.user and (
            obj.status == 'Принята' or view.action == 'create')


class IsDispatcher(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.role == 'Диспетчер'

    def has_object_permission(self, request, view, obj):
        return obj.status == 'Не рассмотрена'


class IsChief(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.role == 'Начальник'

    def has_object_permission(self, request, view, obj):
        return obj.status == 'На рассмотрении'


class IsDriver(permissions.BasePermission):

    def has_permission(self, request, view):
        return request.user.role == 'Водитель'

    def has_object_permission(self, request, view, obj):
        return obj.assigned_driver == request.user
