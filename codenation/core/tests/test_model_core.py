from django.test import TestCase

from codenation.account.models import User
from codenation.core.models import Agent, Event


class AgentModelTest(TestCase):
    def setUp(self) -> None:
        self.agent = Agent.objects.create(
            name="Debian",
            status=True,
            environment="PRODUCTION",
            version='10',
            address="192.168.10.100",
        )

    def test_str(self):
        """Checks if the __str__ method of agent is correct"""
        self.assertEqual(str(self.agent), "PRODUCTION : Debian : 192.168.10.100")


class EventModelTest(TestCase):
    def setUp(self) -> None:
        self.agent = Agent.objects.create(
            name="Debian",
            status=True,
            environment="PRODUCTION",
            version='10',
            address="192.168.10.100",
        )
        self.user = User.objects.create_user(
            first_name="Fulano",
            last_name="de Tal",
            email="fulano@xpto.com",
            password="xpto123",
        )
        self.event = Event.objects.create(
            level="CRITICAL",
            message="ZeroDivisionError: division by zero",
            shelved=True,
            received_in="2020-07-05",
            agent_id=self.agent.pk,
            user_id=self.user.pk
        )

    def test_str(self):
        """Checks if the __str__ method of event is correct"""
        self.assertEqual(str(self.event), "CRITICAL : PRODUCTION : 192.168.10.100")
