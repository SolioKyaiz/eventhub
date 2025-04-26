from rest_framework.routers import DefaultRouter
from .views import TicketViewSet,MyTicketsListView
from django.urls import path, include

router = DefaultRouter()
router.register(r'', TicketViewSet)

urlpatterns = [
    path('my-tickets/', MyTicketsListView.as_view(), name='my-tickets'),
    path('', include(router.urls)),
]
