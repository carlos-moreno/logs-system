from django.test import TestCase

from codenation.account.models import User
from codenation.account.serializers import UserSerializer


class AgentSerializerTest(TestCase):
    def setUp(self) -> None:
        self.expected_results = {
            "id": "4d1cfd50-8580-499e-8033-c58f8d600317",
            "email": "fulano@logsystem.com.br",
            "is_staff": True,
        }
        self.user = User(**self.expected_results)

    def test_expected_serialized_json(self):
        results = UserSerializer(self.user).data
        self.assertEqual(results, self.expected_results)

    def test_raise_error_when_missing_required_field(self):
        incomplete_data = {
            "id": "4d1cfd50-8580-499e-8033-c58f8d600317",
            "email": "fulano@logsystem.com.br",
        }
        serializer = UserSerializer(data=incomplete_data)
        self.assertTrue(serializer.is_valid())
