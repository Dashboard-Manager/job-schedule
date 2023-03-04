# import view sets from the REST framework
from rest_framework import generics, mixins

from apps.presentation_app import models, serializers

# Create your views here.


class PresentationViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView,
):
    serializer_class = serializers.PresentationSerializer
    queryset = models.PresentationModel.objects.all()
    lookup_field = "pk"

    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        text = serializer.validated_data["text"] or None
        if text is None:
            text = "this is a single view doing cool stuff"
        serializer.save(text=text)


class PresentationCreateApiView(
    mixins.CreateModelMixin,
    generics.GenericAPIView,
):
    queryset = models.PresentationModel.objects.all()
    serializer_class = serializers.PresentationSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PresentationDetailApiView(
    generics.RetrieveAPIView,
    mixins.RetrieveModelMixin,
):
    queryset = models.PresentationModel.objects.all()
    serializer_class = serializers.PresentationSerializer

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)


class PresentationListApiView(
    generics.ListAPIView,
    mixins.ListModelMixin,
):
    queryset = models.PresentationModel.objects.all()
    serializer_class = serializers.PresentationSerializer

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)


class PresentationUpdateApiView(
    generics.UpdateAPIView,
    mixins.UpdateModelMixin,
):
    queryset = models.PresentationModel.objects.all()
    serializer_class = serializers.PresentationSerializer
    lookup_field = "pk"

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.title:
            instance.title = "Default Title"


class PresentationDestroyApiView(
    generics.DestroyAPIView,
    mixins.DestroyModelMixin,
):
    queryset = models.PresentationModel.objects.all()
    serializer_class = serializers.PresentationSerializer
    lookup_field = "pk"

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    def preform_destroy(self, instance):
        super().preform_destroy(instance)
