from apps.mision.models import mision, catMedio, catSolicitante, catServicio, catCargo, solicitante, Helicopteros, direccionMision, mision, bitacora, tripulacion, mantenimiento, catSexo, catTipoE

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

class mantenimientoSerializer(serializers.ModelSerializer):

    class Meta:
        model = mantenimiento
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'fechaInicio': instance.fechaInicio,
            'nombre': instance.nombre,
            'apellido1': instance.apellido1,
            'apellido2': instance.apellido2,
            'numeroEmpleado': instance.numeroEmpleado,
            'placaH': instance.helicoptero.placa,
            'helicopteroId': instance.helicoptero.id,
            'modeloH': instance.helicoptero.modelo,

        }

class tripulacionSerializer(serializers.ModelSerializer):

    class Meta:
        model = tripulacion
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'mision': instance.mision,
            'nombre': instance.nombre,
            'apellido1': instance.apellido1,
            'apellido2': instance.apellido2,
            'numeroEmpleado': instance.numeroEmpleado,
        }

class bitacoraSerializer(serializers.ModelSerializer):

    class Meta:
        model = bitacora
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'mision': instance.solicitante,
        }

class direccionMisionSerializer(serializers.ModelSerializer):

    class Meta:
        model = direccionMision
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'calle': instance.calle,
            'colonia': instance.colonia,
            'alcaldia': instance.alcaldia,
            'entidadFederativa': instance.entidadFederativa,
            'coordenadas': instance.coordenadas,
            'poblacionCercana': instance.poblacionCercana,
            'referencia': instance.referencia,
        }

class HelicopterosSerializer(serializers.ModelSerializer):

    class Meta:
        model = Helicopteros
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'placa': instance.placa,
            'modelo': instance.modelo,
            'year': instance.year,
            'marca': instance.marca,
            'status': instance.status,
        }

class HelicopterosSelectSerializer(serializers.ModelSerializer):

    class Meta:
        model = Helicopteros
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'label': instance.placa,
            #'modelo': instance.modelo,
            #'year': instance.year,
            #'marca': instance.marca,
            #'status': instance.status,
        }

class MedioSelectSerializer(serializers.ModelSerializer):

    class Meta:
        model = catMedio
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

class MisionMSelectSerializer(serializers.ModelSerializer):

    class Meta:
        model = direccionMision
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'label': instance.calle,
            #'modelo': instance.modelo,
            #'year': instance.year,
            #'marca': instance.marca,
            #'status': instance.status,
        }

class servicioSelectSerializer(serializers.ModelSerializer):

    class Meta:
        model = catServicio
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

class solicitanteSelectSerializer(serializers.ModelSerializer):

    class Meta:
        model = catSolicitante
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

class sexoSelectSerializer(serializers.ModelSerializer):

    class Meta:
        model = catSexo
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'label': instance.sexo,
            #'modelo': instance.modelo,
            #'year': instance.year,
            #'marca': instance.marca,
            #'status': instance.status,
        }

class tipoESelectSerializer(serializers.ModelSerializer):

    class Meta:
        model = catTipoE
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

class solicitanteSerializer(serializers.ModelSerializer):

    class Meta:
        model = solicitante
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'nombre': instance.nombre,
            'apellido1': instance.apellido1,
            'numeroEmpleado': instance.apellido2,
            'cargo': instance.cargo,
            'telefonoContacto': instance.telefonoContacto,
        }

class catCargoSerializer(serializers.ModelSerializer):

    class Meta:
        model = catCargo
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'nombre': instance.nombre,
        }

class catServicioSerializer(serializers.ModelSerializer):

    class Meta:
        model = catServicio
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'nombre': instance.nombre,
        }

class catSexoSerializer(serializers.ModelSerializer):

    class Meta:
        model = catSexo
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'sexo': instance.sexo,
        }

class catTipoeSerializer(serializers.ModelSerializer):

    class Meta:
        model = catTipoE
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'nombre': instance.nombre,
        }

class catSolicitanteSerializer(serializers.ModelSerializer):

    class Meta:
        model = catSolicitante
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'nombre': instance.nombre,
        }

class catMedioSerializer(serializers.ModelSerializer):

    class Meta:
        model = catMedio
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'nombre': instance.nombre,
        }

class misionSerializer(serializers.ModelSerializer):

    class Meta:
        model = mision
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'medio': instance.medio.nombre,
            'solicitante': instance.solicitante.nombre,
            'servicio': instance.servicio.nombre,
            'ubicacion': instance.ubicacion.colonia,
            'ubicacionID': instance.ubicacion.id,
            'helicoptero': instance.helicoptero.placa,
            'nombre': instance.nombre,
            'apellido1': instance.apellido1,
            'apellido2': instance.apellido2,
            'numeroEmpleado': instance.numeroEmpleado,
            'cuip': instance.cuip,
            'curp': instance.curp,
            'fechaAlta': instance.fechaAlta,
            'fechaNacimiento': instance.fechaNacimiento,
            'rfc': instance.rfc,
            'sexo': instance.sexo.sexo,
            'tipoEmpleado': instance.tipoEmpleado.nombre,
            'helicopteroId': instance.helicoptero.id,
            'sexoId': instance.sexo.id,
            'medioId': instance.medio.id,
            'servicioId': instance.servicio.id,
            'solicitanteId': instance.solicitante.id,
            'tipoEmpleadoId': instance.tipoEmpleado.id,

        }