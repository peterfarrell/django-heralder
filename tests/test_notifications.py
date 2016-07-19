from django.test import TestCase, override_settings

from herald.base import NotificationBase


class BaseNotificationTests(TestCase):
    def test_get_context_data(self):
        class MyNotification(NotificationBase):
            context = {'hello': 'world'}

        with override_settings(DEBUG=True):
            self.assertDictEqual(MyNotification().get_context_data(), {'hello': 'world', 'base_url': ''})

        self.assertDictEqual(MyNotification().get_context_data(), {'hello': 'world', 'base_url': 'http://example.com'})
