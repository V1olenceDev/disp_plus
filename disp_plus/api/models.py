from django.contrib.auth.models import AbstractUser
from django.db import models

from .constants import (
    ORDER_STATUS_CHOICES,
    DEPARTMENT_CHOICES,
    ROLE_CHOICES,
    TRANSPORT_STATUS_CHOICES,
    NOT_CONSIDERED,
    DRIVER,
    AVAILABLE
)


class CustomUser(AbstractUser):
    """
    Модель пользователя.
    """
    role = models.CharField(
        max_length=20,
        verbose_name='Роль',
        choices=ROLE_CHOICES
        )
    department = models.CharField(
        max_length=100,
        verbose_name='Служба',
        choices=DEPARTMENT_CHOICES
        )
    phone_num = models.CharField(
        max_length=15,
        verbose_name='Номер телефона'
        )
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='Группа',
        blank=True,
        related_name="customuser_set",
        related_query_name="user",
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='Пермишены',
        blank=True,
        related_name="customuser_set",
        related_query_name="user",
    )

    def __str__(self):
        return (f"{self.first_name} {self.last_name} - "
                f"{self.get_role_display()}")

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Transport(models.Model):
    """
    Модель техники.
    """
    name = models.CharField(
        max_length=100,
        unique=True,
        verbose_name='Вид транспорта'
        )
    status = models.CharField(
        max_length=15,
        choices=TRANSPORT_STATUS_CHOICES,
        default=AVAILABLE,
        verbose_name='Статус'
        )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Транспорт'
        verbose_name_plural = 'Транспортные средства'


class Order(models.Model):
    """
    Модель заказа.
    """
    creator = models.ForeignKey(
        CustomUser,
        related_name='created_orders',
        on_delete=models.CASCADE,
        verbose_name='Заказчик'
        )
    creation_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания заказа'
        )
    work_date = models.DateField(
        verbose_name='Плнируемая дата работ'
    )
    work_time = models.TimeField(
        verbose_name='Планируемое время работ'
    )
    reason = models.TextField(
        verbose_name='Причина заказа'
    )
    requested_vehicle = models.ForeignKey(
        Transport,
        related_name='requested_orders',
        on_delete=models.SET_NULL,
        null=True,
        verbose_name='Запрошенный транспорт'
        )
    approved_vehicle = models.ForeignKey(
        Transport,
        related_name='approved_orders',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Подтвержденная техника'
        )
    assigned_driver = models.ForeignKey(
        CustomUser,
        related_name='assigned_orders',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        limit_choices_to={'role': DRIVER},
        verbose_name='Водитель'
        )
    status = models.CharField(
        max_length=25,
        choices=ORDER_STATUS_CHOICES,
        default=NOT_CONSIDERED,
        verbose_name='Статус заказа'
        )

    def __str__(self):
        return f"Заказ {self.id} - {self.get_status_display()}"

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
