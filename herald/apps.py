"""
Django app config for herald. Using this to call autodiscover
"""

from django.apps import AppConfig
from django.db.utils import OperationalError


class HeraldConfig(AppConfig):
    """
    Django app config for herald. Using this to call autodiscover
    """

    name = 'herald'

    def ready(self):
        from .models import Notification
        from herald import registry

        self.module.autodiscover()

        try:
            # add any new notifications to database.
            for index, klass in enumerate(registry._registry):
                Notification.objects.get_or_create(notification_class=klass.__name__)
        except OperationalError:
            # if the table is not created yet, just keep going.
            pass
