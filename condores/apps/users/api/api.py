from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from apps.users.models import User
from apps.users.api.serializers import UserSerializer, USerListSerializer

@api_view(['GET','POST'])
def user_api_view(request):
    #en lista
    if request.method == 'GET':
        #busqueda
        users = User.objects.all().values("id", "username", "email", "password")
        users_serializer = USerListSerializer(users, many = True)
        return Response(users_serializer.data, status = status.HTTP_200_OK)
    #crea
    elif request.method == 'POST':
        user_serializer = UserSerializer(data = request.data)
        #validacion
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({'message':'Usuario creado correctamnete'}, status = status.HTTP_201_CREATED)
        return Response(user_serializer.errors, status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def user_details_api_view(request, pk=None):
    #consulta
    user = User.objects.filter(id = pk).first()
    #validacion
    if user:
        #obtener
        if request.method == 'GET':
            user_serializer = UserSerializer(user)
            return Response(user_serializer.data, status = status.HTTP_200_OK)
        #actualizar
        elif request.method == 'PUT':
            user_serializer = UserSerializer(user,data = request.data)
            if user_serializer.is_valid():
                user_serializer.save()
                return Response(user_serializer.data,status = status.HTTP_200_OK)
            return Response(user_serializer.errors, status = status.HTTP_400_BAD_REQUEST)
        #eliminar
        elif request.method == 'DELETE':
            user.delete()
            return Response({'message':'Usuario Eliminado Corrrectamente!!!!'}, status = status.HTTP_200_OK)
    return Response({'message':'No se ha encontrado algun usuario con estos datos'}, status = status.HTTP_400_BAD_REQUEST)
        
            
