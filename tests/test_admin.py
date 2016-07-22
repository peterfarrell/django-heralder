from django.contrib.auth import get_user_model
from django.test import TestCase, Client

from herald.base import NotificationBase


class ViewsTests(TestCase):
    def setUp(self):
        get_user_model().objects.create_superuser('admin', 'admin@example.com', 'password')
        self.client = Client()
        self.client.login(username='admin', password='password')

    def test_index(self):
        response = self.client.get('/admin/herald/sentnotification/')
        self.assertEqual(response.status_code, 200)
