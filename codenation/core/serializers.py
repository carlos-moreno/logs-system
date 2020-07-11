from rest_framework import serializers

from .models import Agent, Event


class AgentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = ["id", "name", "status", "environment", "version", "address"]


class EventSerializer(serializers.ModelSerializer):
    agent_id = serializers.UUIDField()
    user_id = serializers.UUIDField()

    class Meta:
        model = Event
        fields = [
            "id",
            "level",
            "message",
            "shelved",
            "received_in",
            "occurrences",
            "agent_id",
            "user_id",
        ]
