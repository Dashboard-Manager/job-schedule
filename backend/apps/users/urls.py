from apps.users.views import ProfileDetailView
from django.urls import path

urlpatterns = [
    path("profile/<int:identificator>", ProfileDetailView.as_view(), name="profile"),
]
