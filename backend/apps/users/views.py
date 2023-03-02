from apps.users.models import Profile
from django.views.generic import DetailView


class ProfileDetailView(DetailView):
    model = Profile
