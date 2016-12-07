from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics, permissions
from rest_framework_extensions.cache.decorators import (
    cache_response
)
from .models import Config
from .serializers import ConfigSerializer

class ConfigDetail(APIView):
    def get_object(self, uuid):
        try:
            return Config.objects.get(uuid=uuid)
        except Config.DoesNotExist:
            raise Http404

    @cache_response()
    def get(self, request, uuid, format=None):
        config = self.get_object(uuid)
        serializer = ConfigSerializer(config)
        return Response(serializer.data)
