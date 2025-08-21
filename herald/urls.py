from django.urls import re_path

from .views import TestNotification, TestNotificationList


urlpatterns = [
    re_path(r"^$", TestNotificationList.as_view(), name="herald_preview_list"),
    re_path(
        r"^(?P<index>\d+)/(?P<type>[\w\-]+)/$",
        TestNotification.as_view(),
        name="herald_preview",
    ),
]
