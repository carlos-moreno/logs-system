from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import viewsets

from .models import Agent, Event
from .serializers import AgentSerializer, EventSerializer


class AgentViewSet(viewsets.ModelViewSet):
    """Mac doc"""

    queryset = Agent.objects.all()
    serializer_class = AgentSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["environment", "status"]
    search_fields = ["name", "environment", "version", "address"]


class EventViewSet(viewsets.ModelViewSet):
    """Mac doc"""

    queryset = Event.objects.all()
    serializer_class = EventSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["level", "occurrences"]
    search_fields = ["level", "occurrences"]
    ordering_fields = ["level", "occurrences"]
