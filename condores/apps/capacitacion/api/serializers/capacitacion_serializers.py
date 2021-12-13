from apps.capacitacion.models import instructor, cursos, capacitacion

from rest_framework import serializers

from rest_framework_simplejwt.serializers import TokenRefreshSerializer, TokenObtainPairSerializer
from rest_framework_simplejwt.state import token_backend

class CustomTokenSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        # The default result (access/refresh tokens)
        data = super(CustomTokenSerializer, self).validate(attrs)
        # Custom data you want to include
        data.update({'user': self.user.username})
        data.update({'id': self.user.id})
        data.update({'permissions': self.user.permissions.id})
        # and everything else you want to send in the response
        return data

class CustomTokenRefreshSerializer(TokenRefreshSerializer):
    def validate(self, attrs):
        data = super(CustomTokenRefreshSerializer, self).validate(attrs)
        decoded_payload = token_backend.decode(data['access'], verify=True)
        user_uid=decoded_payload['user_id']
        # add filter query
        data.update({'custom_field': 'custom_data'})
        return data

class instructorSerializer(serializers.ModelSerializer):

    class Meta:
        model = instructor
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'nombre': instance.nombre,
            'apellido1': instance.apellido1,
            'apellido2': instance.apellido2,
            'especialidad': instance.especialidad,

        }

class cursoSerializer(serializers.ModelSerializer):

    class Meta:
        model = cursos
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'nombreCurso': instance.nombreCurso,
            'fechaInicio': instance.fechaInicio,
            'fechaFin': instance.fechaFin,
            'instructorNombre': instance.instructor.nombre,
            'instructorId': instance.instructor.id,
            'instructorApellido1': instance.instructor.apellido1,
            'instructorApellido2': instance.instructor.apellido2,
            'instructorEspecialidad': instance.instructor.especialidad,

        }

class cursoSelectSerializer(serializers.ModelSerializer):

    class Meta:
        model = cursos
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'label': instance.nombreCurso,
            #'modelo': instance.modelo,
            #'year': instance.year,
            #'marca': instance.marca,
            #'status': instance.status,
        }

class capacitacionSerializer(serializers.ModelSerializer):

    class Meta:
        model = capacitacion
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'numeroEmpleado': instance.numeroEmpleado,
            
        }

class instructorSelectSerializer(serializers.ModelSerializer):

    class Meta:
        model = instructor
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'label': instance.nombre,
            #'modelo': instance.modelo,
            #'year': instance.year,
            #'marca': instance.marca,
            #'status': instance.status,
        }
