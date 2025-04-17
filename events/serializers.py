from .models import Category,Event
from rest_framework import serializers

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id','title']


class EventSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=True,read_only=True)
    category_ids = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        write_only=True,
        source = 'categories'
    )
    class Meta:
        model = Event
        fields = [
            'id', 'title', 'description', 'location', 'date',
            'category', 'organizer',
            'created_at', 'updated_at','category_ids',
        ]
        read_only_fields = ['organizer', 'created_at', 'updated_at']
