from django.test import TestCase

from herald import registry
from herald.base import EmailNotification


class InitTests(TestCase):
    def test_register(self):
        class TestNotification(EmailNotification):
            pass

        registry.register(TestNotification)

        self.assertEqual(len(registry._registry), 4)

        registry.unregister(TestNotification)

        self.assertEqual(len(registry._registry), 3)

    def test_register_decorator(self):
        @registry.register_decorator()
        class TestNotification(EmailNotification):
            pass

        self.assertEqual(len(registry._registry), 4)
