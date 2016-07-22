from django.test import TestCase, override_settings

from .notifications import MyNotification


class BaseNotificationTests(TestCase):
    def test_get_context_data(self):
        with override_settings(DEBUG=True):
            self.assertDictEqual(
                MyNotification().get_context_data(),
                {'hello': 'world', 'base_url': '', 'subject': None}
            )

        self.assertDictEqual(
            MyNotification().get_context_data(),
            {'hello': 'world', 'base_url': 'http://example.com', 'subject': None}
        )
