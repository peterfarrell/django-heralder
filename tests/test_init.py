from django.test import TestCase

from herald import registry
from herald.base import EmailNotification


class InitTests(TestCase):
    def test_register(self):
        class TestNotification(EmailNotification):
            pass

        registry.register(TestNotification)

        self.assertEqual(len(registry._registry), 7)

        registry.unregister(TestNotification)

        self.assertEqual(len(registry._registry), 6)

    def test_register_decorator(self):
        @registry.register_decorator()
        class TestNotification(EmailNotification):
            pass

        self.assertEqual(len(registry._registry), 7)

        registry.unregister(TestNotification)

        self.assertEqual(len(registry._registry), 6)

    def test_register_invalid(self):
        class TestNotification(object):
            pass

        with self.assertRaises(ValueError):
            registry.register(TestNotification)

        self.assertEqual(len(registry._registry), 6)
