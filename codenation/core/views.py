from django.shortcuts import redirect
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import viewsets

from .models import Agent, Event
from .serializers import AgentSerializer, EventSerializer


class AgentViewSet(viewsets.ModelViewSet):
    """
    list:
    Return a list of all the existing agents.

    create:
    Create a new agent instance.

    retrieve:
    Return the given agent.

    update:
    Update the agent.

    partial_update:
    Update the agent for field.

    delete:
    Delete the agent instance.
    """

    queryset = Agent.objects.all()
    serializer_class = AgentSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ["environment", "status"]
    search_fields = ["name", "environment", "version", "address"]


class EventViewSet(viewsets.ModelViewSet):
    """
    list:
    Return a list of all the existing agents.

    create:
    Create a new agent instance.

    retrieve:
    Return the given agent.

    update:
    Update the agent.

    partial_update:
    Update the agent for field.

    delete:
    Delete the agent instance.
    """

    queryset = Event.objects.all()
    serializer_class = EventSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ["level", "occurrences"]
    search_fields = ["level", "occurrences"]
    ordering_fields = ["level", "occurrences"]


def documentation_api(request):
    return redirect("https://app.swaggerhub.com/apis-docs/carlos-moreno/Logs-System/1.0.0")
