from django.urls import path

from apps.users.views import CreateUserTokenView

urlpatterns = [
    path("users/", CreateUserTokenView.as_view(), name="users"),
]
