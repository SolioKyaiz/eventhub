from rest_framework import viewsets, permissions, filters,status
from .models import Event,Category
from .serializers import EventSerializer, CategorySerializer,ParticipantSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .permissions import IsOrganizerOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response
from tickets.models import Ticket



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

    @action(detail=True, methods=['get'], url_path='participants')
    def get_participants(self, request, pk=None):
        event = self.get_object()
        tickets = Ticket.objects.filter(event=event)
        users = [ticket.user for ticket in tickets]
        serializer = ParticipantSerializer(users, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['delete'], url_path='cancel')
    def cancel_registration(self, request, pk=None):
        user = request.user
        event = self.get_object()

        try:
            ticket = Ticket.objects.get(user=user, event=event)
            ticket.delete()
            return Response({"detail": "Регистрация отменена."}, status=status.HTTP_204_NO_CONTENT)
        except Ticket.DoesNotExist:
            return Response({"detail": "Вы не зарегистрированы на это событие."},
                            status=status.HTTP_400_BAD_REQUEST)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]