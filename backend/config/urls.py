"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

from apps.users import urls as user_urls

urlpatterns = [
    # ADMIN PATHS
    path("admin/", admin.site.urls),
    path("api/auth/", include("dj_rest_auth.urls")),
    path("api/auth/register/", include("dj_rest_auth.registration.urls")),
    path("api/schema/", SpectacularAPIView.as_view(), name="api-schema"),
    path(
        "api/redoc/",
        SpectacularRedocView.as_view(url_name="api-schema"),
        name="api-redoc",
    ),
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="api-schema"),
        name="api-docs",
    ),
    # APPS PATHS
    path(
        "api/earnings/",
        include("apps.earnings.urls"),
        name="earnings",
    ),
    path(
        "api/filesaver/",
        include("apps.filesaver.urls"),
        name="filesaver",
    ),
    path(
        "api/schedules/",
        include("apps.schedules.urls"),
        name="schedules",
    ),
    path(
        "api/workstations/",
        include("apps.workstations.urls"),
        name="workstations",
    ),
    path(
        "api/users/",
        include("apps.users.urls"),
        name="users",
    ),
    path(
        "api/presentation_app/",
        include("apps.presentation_app.urls"),
        name="presentation_app",
    ),
    path(
        "user/",
        include(user_urls),
    ),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += [
        path("debug/", include("debug_toolbar.urls")),
    ]
