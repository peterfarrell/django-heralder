from django.contrib import admin
from django.contrib.auth import urls as auth_urls
from django.urls import include, re_path


urlpatterns = [
    re_path(r"^admin/", admin.site.urls),
    re_path("^", include(auth_urls)),
    re_path(r"^herald/", include("herald.urls")),
]
