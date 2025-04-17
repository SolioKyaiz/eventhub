from rest_framework import viewsets, permissions, filters
from .models import Event,Category
from .serializers import EventSerializer, CategorySerializer
from django_filters.rest_framework import DjangoFilterBackend
from .permissions import IsOrganizerOrReadOnly



class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all().order_by('-date')
    serializer_class = EventSerializer
    permission_classes = [IsOrganizerOrReadOnly]

    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields = ['categories']
    search_fields = ['title','description']
    ordering_fields = ['date','created_at']

    def perform_create(self, serializer):
        serializer.save(organizer = self.request.user)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]