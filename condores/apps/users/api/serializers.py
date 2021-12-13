from rest_framework import serializers
from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__' # todos los campos
        # fields = ['name', 'lasName'.. etc] campos especificos

    def create(self, valite_data):
        user = User(**valite_data)
        user.set_password(valite_data['password'])
        user.save()
        return user
    def update(self, instace, valite_data):
        update_user = super().update(instace, valite_data)
        update_user.set_password(valite_data['password'])
        update_user.save()
        return update_user


        #separar serializador uno para crear y enlistra 
class USerListSerializer(serializers.ModelSerializer):
    class Meta:
        model: User
    def to_representation(self,instance):
        return {
            'id': instance['id'],
            'username': instance['username'],
            'email': instance['email'],
            'password': instance['password']
        }
