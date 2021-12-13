from apps.mision.models import catMedio, catSolicitante, catServicio, catCargo, solicitante,Helicopteros, direccionMision

from rest_framework import serializers

class medioSerializer(serializers.ModelSerializer):

    class Meta:
        model = catMedio
        exclude = ('state', 'created_date')

class solicitanteSerializer(serializers.ModelSerializer):

    class Meta:
        model = catSolicitante
        exclude = ('state',)

class medioSerializer(serializers.ModelSerializer):

    class Meta:
        model = catMedio
        exclude = ('state',)

class servicioSerializer(serializers.ModelSerializer):

    class Meta:
        model = catServicio
        exclude = ('state',)

class cargoSerializer(serializers.ModelSerializer):

    class Meta:
        model = catCargo
        exclude = ('state',)

class solicitanteSerializer(serializers.ModelSerializer):

    class Meta:
        model = solicitante
        exclude = ('state',)

class helicopteroSerializer(serializers.ModelSerializer):

    class Meta:
        model = Helicopteros
        exclude = ('state',)

class direccionMisionSerializer(serializers.ModelSerializer):

    class Meta:
        model = direccionMision
        exclude = ('state',)
