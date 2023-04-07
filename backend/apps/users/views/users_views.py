from rest_framework import generics, permissions
from apps.users.serializers.serializer import UserSerializer
from apps.users.tasks import mails
from rest_framework.response import Response
from rest_framework.reverse import reverse


class CreateUserTokenView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

    def perform_create(self, serializer):
        user = serializer.save()
        mails.send_token_email.delay(user.id)

    def post(self, request, *args, **kwargs):
        response = response = super().post(request, *args, **kwargs)

        url = reverse("users:login")

        return Response(
            response.data,
            status=response.status_code,
            headers={"Location": url},
        )
