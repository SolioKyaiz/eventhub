from rest_framework import serializers
from .models import Ticket
from events.serializers import EventSerializer  # чтобы красиво показать событие

class TicketSerializer(serializers.ModelSerializer):
    event = EventSerializer(read_only=True)  # красиво отображать событие
    event_id = serializers.PrimaryKeyRelatedField(
        queryset=Ticket._meta.get_field('event').remote_field.model.objects.all(),
        write_only=True,
        source='event'
    )

    class Meta:
        model = Ticket
        fields = ['id', 'event', 'event_id', 'created_at']
        read_only_fields = ['id', 'created_at']

    def validate(self, attrs):
        user = self.context['request'].user
        event = attrs['event']

        if Ticket.objects.filter(user=user, event=event).exists():
            raise serializers.ValidationError("Вы уже зарегистрированы на это событие.")

        current_count = Ticket.objects.filter(event=event).count()
        if current_count >= event.capacity:
            raise serializers.ValidationError("Свободных мест больше нет.")

        return attrs