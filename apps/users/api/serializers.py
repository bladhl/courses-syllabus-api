from rest_framework import serializers
from apps.users.models import User


class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ['code', 'id_card', 'name', 'last_name1', 'last_name2', 'email', 'phone', 'password']
  
  def create(self, validated_data):
    user = User(**validated_data)
    user.set_password(validated_data['password'])
    user.save()
    return user


class UserListSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
  
  def to_representation(self, instance):
    return {
      'id': instance['id'],
      'code': instance['code'],
      'id_card': instance['id_card'],
      'name': instance['name'],
      'last_name1': instance['last_name1'],
      'last_name2': instance['last_name2'],
      'email': instance['email'],
      'phone': instance['phone'],
      'category': instance['category']
    }
    

class UpdataUserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = ('name', 'last_name1', 'last_name2', 'email', 'phone')