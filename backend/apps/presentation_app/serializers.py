from rest_framework import serializers

from apps.presentation_app.models import PresentationModel


# create a serializer class
class PresentationSerializer(serializers.ModelSerializer):
    # create a meta class
    class Meta:
        model = PresentationModel
        fields = "__all__"
