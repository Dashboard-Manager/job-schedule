# from django.urls import path
# from django.conf.urls import url
from django.urls import path

from apps.presentation_app import views

urlpatterns = [
    path(
        "presentation",
        views.PresentationViewSet.as_view(),
        name="presentation",
    ),
    path(
        "presentation/create",
        views.PresentationCreateApiView.as_view(),
        name="presentation-create",
    ),
    path(
        "presentation/<int:pk>",
        views.PresentationDetailApiView.as_view(),
        name="presentation-detail",
    ),
    path(
        "presentation/list",
        views.PresentationListApiView.as_view(),
        name="presentation-list",
    ),
    path(
        "presentation/<int:pk>/update/",
        views.PresentationUpdateApiView.as_view(),
        name="presentation-update",
    ),
    path(
        "presentation/<int:pk>/delete/",
        views.PresentationDestroyApiView.as_view(),
        name="presentation-delete",
    ),
]
