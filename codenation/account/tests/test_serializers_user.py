from django.test import TestCase

from codenation.account.models import User
from codenation.account.serializers import UserSerializer


class UserSerializerTest(TestCase):
    def setUp(self) -> None:
        self.expected_results = {
            "id": "ee8eedc1-7f88-4315-91da-724c7d11a136",
            "first_name": "Fulano",
            "last_name": "de Tal",
            "email": "fulano@xpto.com",
        }
        self.user = User(**self.expected_results)

    def test_expected_serialized_json(self):
        results = UserSerializer(self.user).data
        self.assertEqual(results, self.expected_results)

    def test_raise_error_when_missing_required_field(self):
        incomplete_data = {
            "id": "ee8eedc1-7f88-4315-91da-724c7d11a136",
            "first_name": "Fulano",
            "email": "fulano@xpto.com",
        }
        serializer = UserSerializer(data=incomplete_data)
        self.assertFalse(serializer.is_valid())

    def test_validate_password(self):
        """Checks whether it is a valid hash"""
        self.assertTrue(
            UserSerializer.validate_password(
                self.user.password, value=self.user.password
            )
        )
