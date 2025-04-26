from .models import Category,Event
from rest_framework import serializers
from users.models import User
from tickets.models import Ticket

class ParticipantSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','title']


class EventSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True,read_only=True)
    category_ids = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Category.objects.all(),
        write_only=True,
        source = 'categories'
    )
    is_registered = serializers.SerializerMethodField()
    attendance_count = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = [
            'id', 'title', 'description', 'location', 'date',
            'category', 'organizer',
            'created_at', 'updated_at','category_ids','is_registered','capacity','attendance_count'
        ]
        read_only_fields = ['organizer', 'created_at', 'updated_at','is_registered']

    def get_is_registered(self, obj):
        user = self.context['request'].user

        if not user or user.is_anonymous:
            return False

        return Ticket.objects.filter(user=user, event=obj).exists()

    def get_attendance_count(self, obj):
        return obj.tickets.count()

