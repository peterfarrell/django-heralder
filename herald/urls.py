"""
Urls for herald app
"""

try:
    from django.urls import re_path as url
except ImportError:
    from django.conf.urls import url

from django.urls import path
from .views import TestNotificationList, TestNotification, SentNotificationDetail

urlpatterns = [
    path(
        "sent-notification/<int:pk>/",
        SentNotificationDetail.as_view(),
        name="herald_sent_notification_detail",
    ),
    url(r"^$", TestNotificationList.as_view(), name="herald_preview_list"),
    url(
        r"^(?P<index>\d+)/(?P<type>[\w\-]+)/$",
        TestNotification.as_view(),
        name="herald_preview",
    ),
]
