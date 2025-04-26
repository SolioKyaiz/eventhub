from django.db import models
from django.conf import settings
from django.db.models import ForeignKey

from eventhub.settings import AUTH_USER_MODEL


class Category(models.Model):
    title = models.CharField(
        max_length=255,
        unique=True,
        verbose_name='Категория'
    )
    class Meta:
        verbose_name ='Категория'
        verbose_name_plural ='Категории'

    def __str__(self):
        return self.title


class Event(models.Model):
    title = models.CharField(
        max_length=50,
        verbose_name='Название'
    )
    categories = models.ManyToManyField(
        to = Category,
        verbose_name='Категория',
        related_name='events',
    )

    description = models.TextField(
        verbose_name='Описание',
        max_length = 500
    )
    location = models.CharField(
        verbose_name='Локация',
        max_length=255
    )
    date = models.DateTimeField(
        verbose_name='Дата'
    )

    organizer = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='events',
        verbose_name='Организатор'
    )
    capacity = models.PositiveIntegerField(default=100)

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления'
    )



