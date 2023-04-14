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

urlpatterns = [
    # ADMIN PATHS
    path("admin/", admin.site.urls),
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
]

if settings.DEBUG is True:
    urlpatterns += (path("debug/", include("debug_toolbar.urls")),)
    urlpatterns += (path("silk/", include("silk.urls", namespace="silk")),)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
