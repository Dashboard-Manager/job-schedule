from rest_framework import generics, permissions
from apps.users.serializers import UserSerializer
from apps.users.tasks import send_token_email
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.core.exceptions import ValidationError


class CreateUserTokenView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

    def perform_create(self, serializer):
        try:
            user = serializer.save()
            send_token_email.delay(user.id)
        except ValidationError as e:
            raise ValidationError(e.message_dict)

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)

        url = reverse("users:login")

        return Response(
            response.data,
            status=response.status_code,
            headers={"Location": url},
        )
