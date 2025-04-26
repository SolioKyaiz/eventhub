from django.db import models
from django.conf import settings
from eventhub.settings import AUTH_USER_MODEL
from events.models import Event

class Ticket(models.Model):
    user = models.ForeignKey(
        to = settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='tickets',
        verbose_name = 'Пользователь'
    )

    event = models.ForeignKey(
        Event,
        on_delete=models.CASCADE,
        related_name='tickets',
        verbose_name='Мероприятие'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )

    class Meta:
        verbose_name = 'Билет'
        verbose_name_plural = 'Билеты'
        unique_together =('user','event')

    def __str__(self):
        return f"{self.user.email} → {self.event.title}"
