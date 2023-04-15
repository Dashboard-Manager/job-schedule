from django.urls import path

from apps.users import views

urlpatterns = [
    path("create-token/", views.CreateUserTokenView.as_view(), name="create-token"),
]
