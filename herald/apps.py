"""
Django app config for herald. Using this to call autodiscover
"""

import re

from django.apps import AppConfig
from django.db.utils import OperationalError, ProgrammingError


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
            for klass in enumerate(registry._registry):
                if klass.verbose_name:
                    verbose_name = klass.verbose_name
                else:
                    verbose_name = re.sub(
                        r'((?<=[a-z])[A-Z]|(?<!\A)[A-Z](?=[a-z]))',
                        r' \1',
                        klass.__name__
                    )

                notification, created = Notification.objects.get_or_create(notification_class=klass.__name__)
                if created:
                    notification.verbose_name = verbose_name
                    notification.can_disable = klass.can_disable
                    notification.save()

        except OperationalError:
            # if the table is not created yet, just keep going.
            pass
        except ProgrammingError:
            # if the database is not created yet, keep going (ie: during testing)
            pass
