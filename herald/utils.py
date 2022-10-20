from django.apps import apps as django_apps
from django.core.exceptions import ImproperlyConfigured

from herald.conf import settings as herald_settings


def get_sent_notification_model():
    try:
        return django_apps.get_model(herald_settings.SENT_NOTIFICATION_MODEL)
    except ValueError:
        raise ImproperlyConfigured(
            "SENT_NOTIFICATION_MODEL must be of the form 'app_label.model_name'"
        )
    except LookupError:
        raise ImproperlyConfigured(
            f"SENT_NOTIFICATION_MODEL refers to model '{herald_settings.SENT_NOTIFICATION_MODEL}' that has not been installed"
        )
