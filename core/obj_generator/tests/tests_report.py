import os
from django.test import SimpleTestCase
from django.conf import settings

from rest_framework.test import APIClient
from rest_framework import status


REPORT_URL = '/api/report/'


class TestReport(SimpleTestCase):

    def setUp(self) -> None:
        self.client = APIClient()

    def test_generated_object_size(self):
        size = int(os.path.getsize(f"{settings.BASE_DIR}/media/data/objects.txt")) / 1048576
        self.assertLessEqual(size, 2.0)

    def test_get_report(self):
        res = self.client.get(REPORT_URL)
        self.assertIn("string", res.data)
        self.assertIn("real_number", res.data)
        self.assertIn("integers", res.data)
        self.assertIn("alphanumerics", res.data)
        self.assertNotIn("positive_integers", res.data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
