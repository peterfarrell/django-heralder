from __future__ import absolute_import
from __future__ import unicode_literals

from django.contrib import admin
from django.conf.urls import url, include


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^herald/', include('herald.urls')),
]
