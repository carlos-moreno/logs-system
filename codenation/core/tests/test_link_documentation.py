from django.shortcuts import resolve_url as r
from django.test import TestCase


class AgentSerializerTest(TestCase):
    def setUp(self) -> None:
        self.link = (
            "https://app.swaggerhub.com/apis-docs/carlos-moreno/Logs-System/1.0.0"
        )

    def test_link(self):
        doc = self.client.get(r("documentation"))
        self.assertEqual(self.link, doc.url)
