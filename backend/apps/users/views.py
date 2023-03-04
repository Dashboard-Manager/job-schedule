from django.views.generic import DetailView

from apps.users.models import Profile


class ProfileDetailView(DetailView):
    model = Profile
