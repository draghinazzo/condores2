from django_filters.filters import OrderingFilter
import rest_framework
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from apps.base.api import generalListApiView
from apps.mision.api.serializers.mision_serializers import catMedioSerializer, catSolicitanteSerializer,catServicioSerializer, catCargoSerializer, CustomTokenRefreshSerializer, CustomTokenSerializer, catSexoSerializer, catTipoeSerializer, MedioSelectSerializer, servicioSelectSerializer, solicitanteSelectSerializer, sexoSelectSerializer, tipoESelectSerializer, catInstitucionSerializer, personaSerializer, intructoresSerializer, descripcionEmergenciaSerializer, solicitudEmergenciaSerializer, institucionSelectSerializer, puenteEmergenciaSerializer
"""
HelicopterosSelectSerializer, misionSerializer, solicitanteSerializer, HelicopterosSerializer, direccionMisionSerializer, bitacoraSerializer, tripulacionSerializer, mantenimientoSerializer, MisionMSelectSerializer
"""
from rest_framework import generics,status
from rest_framework import viewsets
from apps.mision.api.filtros.catalogosFilter import catMedioFilters, catCargoFilters, catCServicioFilters, catCSolicitanteFilters, catSexoFilters, catTipoeFilters
from django_filters.rest_framework import DjangoFilterBackend


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
"""
class mantenimientoViewSet(viewsets.ModelViewSet,APIView):
    serializer_class = mantenimientoSerializer
    queryset = mantenimientoSerializer.Meta.model.objects.filter(state = True)
    permission_classes = [IsAuthenticated]

    def destroy(self, request,pk=None):
        mision = self.get_queryset().filter(id=pk).first()
        if mision:
            mision.state = False
            mision.save()
            return Response({'message': 'mision eliminada correctamente'}, status = status.HTTP_200_OK)
        return Response({'error': 'No existe dato'}, status = status.HTTP_400_BAD_REQUEST)

class tripulacionViewSet(viewsets.ModelViewSet,APIView):
    serializer_class = tripulacionSerializer
    queryset = tripulacionSerializer.Meta.model.objects.filter(state = True)
    permission_classes = [IsAuthenticated]

    def destroy(self, request,pk=None):
        mision = self.get_queryset().filter(id=pk).first()
        if mision:
            mision.state = False
            mision.save()
            return Response({'message': 'mision eliminada correctamente'}, status = status.HTTP_200_OK)
        return Response({'error': 'No existe dato'}, status = status.HTTP_400_BAD_REQUEST)        

class bitacoraViewSet(viewsets.ModelViewSet,APIView):
    serializer_class = bitacoraSerializer
    queryset = bitacoraSerializer.Meta.model.objects.filter(state = True)
    permission_classes = [IsAuthenticated]

    def destroy(self, request,pk=None):
        mision = self.get_queryset().filter(id=pk).first()
        if mision:
            mision.state = False
            mision.save()
            return Response({'message': 'mision eliminada correctamente'}, status = status.HTTP_200_OK)
        return Response({'error': 'No existe dato'}, status = status.HTTP_400_BAD_REQUEST)

class direccionMisionViewSet(viewsets.ModelViewSet,APIView):
    serializer_class = direccionMisionSerializer
    queryset = direccionMisionSerializer.Meta.model.objects.filter(state = True)
    permission_classes = [IsAuthenticated]

    def destroy(self, request,pk=None):
        mision = self.get_queryset().filter(id=pk).first()
        if mision:
            mision.state = False
            mision.save()
            return Response({'message': 'mision eliminada correctamente'}, status = status.HTTP_200_OK)
        return Response({'error': 'No existe dato'}, status = status.HTTP_400_BAD_REQUEST)

class HelicopterosViewSet(viewsets.ModelViewSet,APIView):
    serializer_class = HelicopterosSerializer
    queryset = HelicopterosSerializer.Meta.model.objects.filter(state = True)
    permission_classes = [IsAuthenticated]

    def destroy(self, request,pk=None):
        mision = self.get_queryset().filter(id=pk).first()
        if mision:
            mision.state = False
            mision.save()
            return Response({'message': 'mision eliminada correctamente'}, status = status.HTTP_200_OK)
        return Response({'error': 'No existe dato'}, status = status.HTTP_400_BAD_REQUEST)

class HelicopterosSelectViewSet(viewsets.ModelViewSet,APIView):
    serializer_class = HelicopterosSelectSerializer
    queryset = HelicopterosSelectSerializer.Meta.model.objects.filter(state = True)
    permission_classes = [IsAuthenticated]

    def destroy(self, request,pk=None):
        mision = self.get_queryset().filter(id=pk).first()
        if mision:
            mision.state = False
            mision.save()
            return Response({'message': 'mision eliminada correctamente'}, status = status.HTTP_200_OK)
        return Response({'error': 'No existe dato'}, status = status.HTTP_400_BAD_REQUEST)

class direccionMSelectisionViewSet(viewsets.ModelViewSet,APIView):
    serializer_class = MisionMSelectSerializer
    queryset = MisionMSelectSerializer.Meta.model.objects.filter(state = True)
    permission_classes = [IsAuthenticated]

    def destroy(self, request,pk=None):
        mision = self.get_queryset().filter(id=pk).first()
        if mision:
            mision.state = False
            mision.save()
            return Response({'message': 'mision eliminada correctamente'}, status = status.HTTP_200_OK)
        return Response({'error': 'No existe dato'}, status = status.HTTP_400_BAD_REQUEST)     
"""
class medioSelectViewSet(viewsets.ModelViewSet,APIView):
    serializer_class = MedioSelectSerializer
    queryset = MedioSelectSerializer.Meta.model.objects.filter(state = True)
    permission_classes = [IsAuthenticated]

    def destroy(self, request,pk=None):
        mision = self.get_queryset().filter(id=pk).first()
        if mision:
            mision.state = False
            mision.save()
            return Response({'message': 'mision eliminada correctamente'}, status = status.HTTP_200_OK)
        return Response({'error': 'No existe dato'}, status = status.HTTP_400_BAD_REQUEST)     

class servicioSelectViewSet(viewsets.ModelViewSet,APIView):
    serializer_class = servicioSelectSerializer
    queryset = servicioSelectSerializer.Meta.model.objects.filter(state = True)
    permission_classes = [IsAuthenticated]

    def destroy(self, request,pk=None):
        mision = self.get_queryset().filter(id=pk).first()
        if mision:
            mision.state = False
            mision.save()
            return Response({'message': 'mision eliminada correctamente'}, status = status.HTTP_200_OK)
        return Response({'error': 'No existe dato'}, status = status.HTTP_400_BAD_REQUEST)     

class solicitanteSelectViewSet(viewsets.ModelViewSet,APIView):
    serializer_class = solicitanteSelectSerializer
    queryset = solicitanteSelectSerializer.Meta.model.objects.filter(state = True)
    permission_classes = [IsAuthenticated]

    def destroy(self, request,pk=None):
        mision = self.get_queryset().filter(id=pk).first()
        if mision:
            mision.state = False
            mision.save()
            return Response({'message': 'mision eliminada correctamente'}, status = status.HTTP_200_OK)
        return Response({'error': 'No existe dato'}, status = status.HTTP_400_BAD_REQUEST)     

class sexoSelectViewSet(viewsets.ModelViewSet,APIView):
    serializer_class = sexoSelectSerializer
    queryset = sexoSelectSerializer.Meta.model.objects.filter(state = True)
    permission_classes = [IsAuthenticated]

    def destroy(self, request,pk=None):
        mision = self.get_queryset().filter(id=pk).first()
        if mision:
            mision.state = False
            mision.save()
            return Response({'message': 'mision eliminada correctamente'}, status = status.HTTP_200_OK)
        return Response({'error': 'No existe dato'}, status = status.HTTP_400_BAD_REQUEST)     

class tipoESelectViewSet(viewsets.ModelViewSet,APIView):
    serializer_class = tipoESelectSerializer
    queryset = tipoESelectSerializer.Meta.model.objects.filter(state = True)
    permission_classes = [IsAuthenticated]

    def destroy(self, request,pk=None):
        mision = self.get_queryset().filter(id=pk).first()
        if mision:
            mision.state = False
            mision.save()
            return Response({'message': 'mision eliminada correctamente'}, status = status.HTTP_200_OK)
        return Response({'error': 'No existe dato'}, status = status.HTTP_400_BAD_REQUEST)  

class solicitanteViewSet(viewsets.ModelViewSet,APIView):
    serializer_class = catSolicitanteSerializer
    queryset = catSolicitanteSerializer.Meta.model.objects.filter(state = True)
    permission_classes = [IsAuthenticated]

    def destroy(self, request,pk=None):
        mision = self.get_queryset().filter(id=pk).first()
        if mision:
            mision.state = False
            mision.save()
            return Response({'message': 'mision eliminada correctamente'}, status = status.HTTP_200_OK)
        return Response({'error': 'No existe dato'}, status = status.HTTP_400_BAD_REQUEST)

class catCargoViewSet(viewsets.ModelViewSet,APIView):
    serializer_class = catCargoSerializer
    queryset = catCargoSerializer.Meta.model.objects.filter(state = True).order_by('id')
    #queryset = catMedioSerializer.Meta.model.objects.order_by('id')
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend,]
    filterset_class = catCargoFilters
    ordering_fields = [
        "id",
        "nombre",
    ]

    def destroy(self, request,pk=None):
        mision = self.get_queryset().filter(id=pk).first()
        if mision:
            mision.state = False
            mision.save()
            return Response({'message': 'mision eliminada correctamente'}, status = status.HTTP_200_OK)
        return Response({'error': 'No existe dato'}, status = status.HTTP_400_BAD_REQUEST)

class catServicioViewSet(viewsets.ModelViewSet,APIView):
    serializer_class = catServicioSerializer
    queryset = catServicioSerializer.Meta.model.objects.filter(state = True).order_by('id')
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend,]
    filterset_class = catCServicioFilters
    ordering_fields = [
        "id",
        "nombre",
    ]

    def destroy(self, request,pk=None):
        mision = self.get_queryset().filter(id=pk).first()
        if mision:
            mision.state = False
            mision.save()
            return Response({'message': 'mision eliminada correctamente'}, status = status.HTTP_200_OK)
        return Response({'error': 'No existe dato'}, status = status.HTTP_400_BAD_REQUEST)

class catSexoViewSet(viewsets.ModelViewSet,APIView):
    serializer_class = catSexoSerializer
    queryset = catSexoSerializer.Meta.model.objects.filter(state = True).order_by('id')
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend,]
    filterset_class = catSexoFilters
    ordering_fields = [
        "id",
        "sexo",
    ]

    def destroy(self, request,pk=None):
        mision = self.get_queryset().filter(id=pk).first()
        if mision:
            mision.state = False
            mision.save()
            return Response({'message': 'mision eliminada correctamente'}, status = status.HTTP_200_OK)
        return Response({'error': 'No existe dato'}, status = status.HTTP_400_BAD_REQUEST)

class catTipoeViewSet(viewsets.ModelViewSet,APIView):
    serializer_class = catTipoeSerializer
    queryset = catTipoeSerializer.Meta.model.objects.filter(state = True).order_by('id')
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend,]
    filterset_class = catTipoeFilters
    ordering_fields = [
        "id",
        "nombre",
    ]

    def destroy(self, request,pk=None):
        mision = self.get_queryset().filter(id=pk).first()
        if mision:
            mision.state = False
            mision.save()
            return Response({'message': 'mision eliminada correctamente'}, status = status.HTTP_200_OK)
        return Response({'error': 'No existe dato'}, status = status.HTTP_400_BAD_REQUEST)

class catSolicitanteViewSet(viewsets.ModelViewSet,APIView):
    serializer_class = catSolicitanteSerializer
    queryset = catSolicitanteSerializer.Meta.model.objects.filter(state = True)
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend,]
    filterset_class = catCSolicitanteFilters
    ordering_fields = [
        "id",
        "nombre",
    ]

    def destroy(self, request,pk=None):
        mision = self.get_queryset().filter(id=pk).first()
        if mision:
            mision.state = False
            mision.save()
            return Response({'message': 'mision eliminada correctamente'}, status = status.HTTP_200_OK)
        return Response({'error': 'No existe dato'}, status = status.HTTP_400_BAD_REQUEST)

class catMedioViewSet(viewsets.ModelViewSet,APIView):
    serializer_class = catMedioSerializer
    queryset = catMedioSerializer.Meta.model.objects.filter(state = True).order_by('id')
    #queryset = catMedioSerializer.Meta.model.objects.order_by('id')
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend,]
    filterset_class = catMedioFilters
    ordering_fields = [
        "id",
        "nombre",
    ]

    #def list(self, request):
    #    medio_serializer = self.get_serializer(self.get_queryset(), many = True)
    #    return Response(medio_serializer.data, status = status.HTTP_200_OK)

    def destroy(self, request,pk=None):
        mision = self.get_queryset().filter(id=pk).first()
        if mision:
            mision.state = False
            mision.save()
            return Response({'message': 'mision eliminada correctamente'}, status = status.HTTP_200_OK)
        return Response({'error': 'No existe dato'}, status = status.HTTP_400_BAD_REQUEST)

class institucionctViewSet(viewsets.ModelViewSet,APIView):
    serializer_class = institucionSelectSerializer
    queryset = institucionSelectSerializer.Meta.model.objects.filter(state = True)
    permission_classes = [IsAuthenticated]

    def destroy(self, request,pk=None):
        mision = self.get_queryset().filter(id=pk).first()
        if mision:
            mision.state = False
            mision.save()
            return Response({'message': 'mision eliminada correctamente'}, status = status.HTTP_200_OK)
        return Response({'error': 'No existe dato'}, status = status.HTTP_400_BAD_REQUEST)   

class catInstitucionViewSet(viewsets.ModelViewSet,APIView):
    serializer_class = catInstitucionSerializer
    queryset = catInstitucionSerializer.Meta.model.objects.filter(state = True).order_by('id')
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend,]
    #filterset_class = catMedioFilters
    #ordering_fields = [
    #    "id",
    #    "nombre",
    #]

    #def list(self, request):
    #    medio_serializer = self.get_serializer(self.get_queryset(), many = True)
    #    return Response(medio_serializer.data, status = status.HTTP_200_OK)

    def destroy(self, request,pk=None):
        mision = self.get_queryset().filter(id=pk).first()
        if mision:
            mision.state = False
            mision.save()
            return Response({'message': 'mision eliminada correctamente'}, status = status.HTTP_200_OK)
        return Response({'error': 'No existe dato'}, status = status.HTTP_400_BAD_REQUEST)    

class personaViewSet(viewsets.ModelViewSet,APIView):
    serializer_class = personaSerializer
    queryset = personaSerializer.Meta.model.objects.filter(state = True).order_by('id')
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend,]
    #filterset_class = catMedioFilters
    #ordering_fields = [
    #    "id",
    #    "nombre",
    #]

    #def list(self, request):
    #    medio_serializer = self.get_serializer(self.get_queryset(), many = True)
    #    return Response(medio_serializer.data, status = status.HTTP_200_OK)

    def destroy(self, request,pk=None):
        mision = self.get_queryset().filter(id=pk).first()
        if mision:
            mision.state = False
            mision.save()
            return Response({'message': 'mision eliminada correctamente'}, status = status.HTTP_200_OK)
        return Response({'error': 'No existe dato'}, status = status.HTTP_400_BAD_REQUEST)  

class intructoresViewSet(viewsets.ModelViewSet,APIView):
    serializer_class = intructoresSerializer
    queryset = intructoresSerializer.Meta.model.objects.filter(state = True).order_by('id')
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend,]
    #filterset_class = catMedioFilters
    #ordering_fields = [
    #    "id",
    #    "nombre",
    #]

    #def list(self, request):
    #    medio_serializer = self.get_serializer(self.get_queryset(), many = True)
    #    return Response(medio_serializer.data, status = status.HTTP_200_OK)

    def destroy(self, request,pk=None):
        mision = self.get_queryset().filter(id=pk).first()
        if mision:
            mision.state = False
            mision.save()
            return Response({'message': 'mision eliminada correctamente'}, status = status.HTTP_200_OK)
        return Response({'error': 'No existe dato'}, status = status.HTTP_400_BAD_REQUEST)    

class descripcionEmergenciaViewSet(viewsets.ModelViewSet,APIView):
    serializer_class = descripcionEmergenciaSerializer
    queryset = descripcionEmergenciaSerializer.Meta.model.objects.filter(state = True).order_by('id')
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend,]
    #filterset_class = catMedioFilters
    #ordering_fields = [
    #    "id",
    #    "nombre",
    #]

    #def list(self, request):
    #    medio_serializer = self.get_serializer(self.get_queryset(), many = True)
    #    return Response(medio_serializer.data, status = status.HTTP_200_OK)

    def destroy(self, request,pk=None):
        mision = self.get_queryset().filter(id=pk).first()
        if mision:
            mision.state = False
            mision.save()
            return Response({'message': 'mision eliminada correctamente'}, status = status.HTTP_200_OK)
        return Response({'error': 'No existe dato'}, status = status.HTTP_400_BAD_REQUEST)  

class solicitudEmergenciaViewSet(viewsets.ModelViewSet,APIView):
    serializer_class = solicitudEmergenciaSerializer
    queryset = solicitudEmergenciaSerializer.Meta.model.objects.filter(state = True).order_by('id')
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend,]
    #filterset_class = catMedioFilters
    #ordering_fields = [
    #    "id",
    #    "nombre",
    #]

    #def list(self, request):
    #    medio_serializer = self.get_serializer(self.get_queryset(), many = True)
    #    return Response(medio_serializer.data, status = status.HTTP_200_OK)

    def destroy(self, request,pk=None):
        mision = self.get_queryset().filter(id=pk).first()
        if mision:
            mision.state = False
            mision.save()
            return Response({'message': 'mision eliminada correctamente'}, status = status.HTTP_200_OK)
        return Response({'error': 'No existe dato'}, status = status.HTTP_400_BAD_REQUEST) 

class puenteEmergenciaViewSet(viewsets.ModelViewSet,APIView):
    serializer_class = puenteEmergenciaSerializer
    queryset = puenteEmergenciaSerializer.Meta.model.objects.filter(state = True).order_by('id')
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend,]
    #filterset_class = catMedioFilters
    #ordering_fields = [
    #    "id",
    #    "nombre",
    #]

    #def list(self, request):
    #    medio_serializer = self.get_serializer(self.get_queryset(), many = True)
    #    return Response(medio_serializer.data, status = status.HTTP_200_OK)

    def destroy(self, request,pk=None):
        mision = self.get_queryset().filter(id=pk).first()
        if mision:
            mision.state = False
            mision.save()
            return Response({'message': 'mision eliminada correctamente'}, status = status.HTTP_200_OK)
        return Response({'error': 'No existe dato'}, status = status.HTTP_400_BAD_REQUEST) 
                       
"""
class misionViewSet(viewsets.ModelViewSet):
    serializer_class = misionSerializer
    queryset = misionSerializer.Meta.model.objects.filter(state = True)

    #def list(self,request):
    #    return Response({'mensaje':'holaaaaaaaaaaaaaaaaaa'})

#class misionCreateAPIView(generics.CreateAPIView):

class misionListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = misionSerializer
    queryset = misionSerializer.Meta.model.objects.filter(state = True)

    def post(self, request):
        serializers = self.serializer_class(data = request.data)
        if serializers.is_valid():
            serializers.save()
            return Response({'message': 'Mision creada correctamente'}, status = status.HTTP_201_CREATED)
        return Response(serializers.errors, status = status.HTTP_400_BAD_REQUEST)

class misionRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = misionSerializer

    def get_queryset(self, pk=None):
        if pk is None:
            return self.get_serializer().Meta.model.objects.filter(state = True)
        else:
            return self.get_serializer().Meta.model.objects.filter(id = pk, state = True).first()
    
    def put(self, request, pk=None):
        if self.get_queryset(pk):
            mision_serializer = self.serializer_class(self.get_queryset(pk), data = request.data)
            if mision_serializer.is_valid():
                mision_serializer.save()
                return Response(mision_serializer.data, status = status.HTTP_200_OK)
            return Response(mision_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request,pk=None):
        mision = self.get_queryset().filter(id=pk).first()
        if mision:
            mision.state = False
            mision.save()
            return Response({'message': 'mision eliminada correctamente'}, status = status.HTTP_200_OK)
        return Response({'error': 'No existe dato'}, status = status.HTTP_400_BAD_REQUEST)
    
    def patch(self, request, pk=None):
        if self.get_queryset(pk):
            mision_serializer = self.serializer_class(self.get_queryset(pk))
            return Response(mision_serializer.data, status = status.HTTP_200_OK)
        return Response({'error': 'No existe dato'}, status = status.HTTP_400_BAD_REQUEST)

    def put(self, request, pk=None):
        if self.get_queryset(pk):
            mision_serializer = self.serializer_class(self.get_queryset(pk), data= request.data)
            if mision_serializer.is_valid():
                mision_serializer.save()
                return Response(mision_serializer.data, status = status.HTTP_200_OK)
            return Response(mision_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
"""


