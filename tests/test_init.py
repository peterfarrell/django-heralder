from django.test import TestCase

from herald import registry
from herald.base import EmailNotification


class InitTests(TestCase):
    def test_register(self):
        class TestNotification(EmailNotification):
            pass

        oldvalue = len(registry._registry)

        registry.register(TestNotification)

        self.assertEqual(len(registry._registry), oldvalue + 1)

        registry.unregister(TestNotification)

        self.assertEqual(len(registry._registry), oldvalue)
