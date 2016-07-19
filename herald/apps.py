"""
Django app config for herald. Using this to call autodiscover
"""

from django.apps import AppConfig


class HeraldConfig(AppConfig):
    """
    Django app config for herald. Using this to call autodiscover
    """

    name = 'herald'

    def ready(self):
        self.module.autodiscover()
