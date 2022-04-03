from unittest.mock import patch

from django.test import SimpleTestCase
from rest_framework.test import APIClient
from rest_framework import status

from ..services import ObjGenerator


OBJ_GENERATOR_URL = '/api/generate-obj/'


class TestObjGenerator(SimpleTestCase):

    def setUp(self) -> None:
        self.client = APIClient()

    def test_home(self):
        res = self.client.get("/")
        self.assertEqual(res.status_code, 200)

    @patch.object(ObjGenerator, 'generate_obj_process')
    def test_generator_running(self, mocked_obj_generator):
        res = self.client.get(OBJ_GENERATOR_URL)
        mocked_obj_generator.return_value = {"file_link": res.wsgi_request.build_absolute_uri('/media/data/objects.txt')}
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data.get('file_link'), 'http://testserver/media/data/objects.txt')

    def test_generate_obj_type(self):
        obj_generator = ObjGenerator()
        self.assertIsInstance(int(obj_generator.generate_integers()), int)
        self.assertIsInstance(obj_generator.generate_alpha_string(), str)
        self.assertTrue(str.isalnum(obj_generator.generate_alphanumerics()))
        self.assertNotIsInstance(obj_generator.generate_real_number(), int)
