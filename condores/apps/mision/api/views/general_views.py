from apps.base.api import generalListApiView
from apps.mision.api.serializers.general_serializer import medioSerializer

class medioListAPIView(generalListApiView):
    serializer_class = medioSerializer
