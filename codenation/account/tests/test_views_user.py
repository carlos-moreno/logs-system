from django.shortcuts import resolve_url as r
from django.test import TestCase
from rest_framework.test import APIClient

from codenation.account.models import User


class UserViewTest(TestCase):

    def setUp(self):
        self.client = APIClient()
        self.resp = r("/api/v1/users/")
        self.data = {
            "first_name": "Fulano",
            "last_name": "de Tal",
            "email": "fulano@xpto.com",
            "password": "fulano123"
        }

    def test_get(self):
        """GET /api/v1/users must return status code 200"""
        resp = self.client.get(self.resp)
        self.assertEqual(resp.status_code, 200)

    def test_post(self):
        """POST /api/v1/users with the correct data should return 201"""
        resp = self.client.post(self.resp, self.data)
        self.assertEqual(resp.status_code, 201)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(User.objects.get().get_full_name(), 'Fulano de Tal')
