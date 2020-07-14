from django.test import TestCase

from codenation.core.models import Agent, Event
from codenation.core.serializers import AgentSerializer, EventSerializer


class AgentSerializerTest(TestCase):
    def setUp(self) -> None:
        self.expected_results = {
            "id": "4d1cfd50-8580-499e-8033-c58f8d600317",
            "name": "Debian",
            "status": True,
            "environment": "PRODUCTION",
            "version": '10',
            "address": "192.168.10.100",
        }
        self.agent = Agent(**self.expected_results)

    def test_expected_serialized_json(self):
        results = AgentSerializer(self.agent).data
        self.assertEqual(results, self.expected_results)

    def test_raise_error_when_missing_required_field(self):
        incomplete_data = {
            "name": "Debian",
            "status": True,
            "environment": "PRODUCTION",
            "version": "10",
            "address": "192.168.10.100",
        }
        serializer = AgentSerializer(data=incomplete_data)
        self.assertTrue(serializer.is_valid())


class EventSerializerTest(TestCase):

    def setUp(self) -> None:
        self.expected_results = {
            "id": "fe243ac0-dc29-44d5-8362-b0d35a131826",
            "level": "CRITICAL",
            "message": "ZeroDivisionError: division by zero",
            "shelved": True,
            "received_in": "2020-07-05",
            "occurrences": 2,
            "agent_id": "a86224d6-d1a5-4a6c-8b23-4e346b59ff3d",
            "user_id": "ad449688-3c1f-4845-a9d2-4270623d7e01",
        }
        self.event = Event(**self.expected_results)

    def test_expected_serialized_json(self):
        results = EventSerializer(self.event).data
        self.assertEqual(results, self.expected_results)

    def test_raise_error_when_missing_required_field(self):
        incomplete_data = {
            "level": "CRITICAL",
            "message": "ZeroDivisionError: division by zero",
            "shelved": True,
            "received_in": "2020-07-05",
            "occurrences": 2,
            "agent_id": "a86224d6-d1a5-4a6c-8b23-4e346b59ff3d",
            "user_id": "ad449688-3c1f-4845-a9d2-4270623d7e01",
        }
        serializer = EventSerializer(data=incomplete_data)
        self.assertTrue(serializer.is_valid())
