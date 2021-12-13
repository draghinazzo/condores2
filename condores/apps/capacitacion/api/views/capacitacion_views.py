from django_filters.filters import OrderingFilter
import rest_framework
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from apps.base.api import generalListApiView
from apps.capacitacion.api.serializers.capacitacion_serializers import instructorSerializer, CustomTokenRefreshSerializer, CustomTokenSerializer, cursoSerializer, instructorSelectSerializer, capacitacionSerializer, cursoSelectSerializer
from rest_framework import generics,status
from rest_framework import viewsets


class CustomTokenView(TokenObtainPairView):
    """
    Custom Refresh token View
    """
    serializer_class = CustomTokenSerializer

class CustomTokenRefreshView(TokenRefreshView):
    """
    Custom Refresh token View
    """
    serializer_class = CustomTokenRefreshSerializer

class instructorViewSet(viewsets.ModelViewSet,APIView):
    serializer_class = instructorSerializer
    queryset = instructorSerializer.Meta.model.objects.filter(state = True)
    permission_classes = [IsAuthenticated]

    def destroy(self, request,pk=None):
        mision = self.get_queryset().filter(id=pk).first()
        if mision:
            mision.state = False
            mision.save()
            return Response({'message': 'mision eliminada correctamente'}, status = status.HTTP_200_OK)
        return Response({'error': 'No existe dato'}, status = status.HTTP_400_BAD_REQUEST)

class cursoViewSet(viewsets.ModelViewSet,APIView):
    serializer_class = cursoSerializer
    queryset = cursoSerializer.Meta.model.objects.filter(state = True)
    permission_classes = [IsAuthenticated]

    def destroy(self, request,pk=None):
        mision = self.get_queryset().filter(id=pk).first()
        if mision:
            mision.state = False
            mision.save()
            return Response({'message': 'mision eliminada correctamente'}, status = status.HTTP_200_OK)
        return Response({'error': 'No existe dato'}, status = status.HTTP_400_BAD_REQUEST)

class cursoSelectViewSet(viewsets.ModelViewSet,APIView):
    serializer_class = cursoSelectSerializer
    queryset = cursoSelectSerializer.Meta.model.objects.filter(state = True)
    permission_classes = [IsAuthenticated]

    def destroy(self, request,pk=None):
        mision = self.get_queryset().filter(id=pk).first()
        if mision:
            mision.state = False
            mision.save()
            return Response({'message': 'mision eliminada correctamente'}, status = status.HTTP_200_OK)
        return Response({'error': 'No existe dato'}, status = status.HTTP_400_BAD_REQUEST)   

class capacitacionViewSet(viewsets.ModelViewSet,APIView):
    serializer_class = capacitacionSerializer
    queryset = capacitacionSerializer.Meta.model.objects.filter(state = True)
    permission_classes = [IsAuthenticated]

    def destroy(self, request,pk=None):
        mision = self.get_queryset().filter(id=pk).first()
        if mision:
            mision.state = False
            mision.save()
            return Response({'message': 'mision eliminada correctamente'}, status = status.HTTP_200_OK)
        return Response({'error': 'No existe dato'}, status = status.HTTP_400_BAD_REQUEST)        

class instructorSelectViewSet(viewsets.ModelViewSet,APIView):
    serializer_class = instructorSelectSerializer
    queryset = instructorSelectSerializer.Meta.model.objects.filter(state = True)
    permission_classes = [IsAuthenticated]

    def destroy(self, request,pk=None):
        mision = self.get_queryset().filter(id=pk).first()
        if mision:
            mision.state = False
            mision.save()
            return Response({'message': 'mision eliminada correctamente'}, status = status.HTTP_200_OK)
        return Response({'error': 'No existe dato'}, status = status.HTTP_400_BAD_REQUEST)


