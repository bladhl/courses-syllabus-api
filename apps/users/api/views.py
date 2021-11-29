from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response

from apps.users.models import User
from apps.users.api.serializers import UserSerializer, UserListSerializer, UpdataUserSerializer


class UserViewSet(viewsets.ModelViewSet):
  model = User
  serializer_class = UserSerializer
  list_serializer_class = UserListSerializer
  
  def get_queryset(self):
    if self.queryset is None:
      self.queryset = self.model.objects.filter(is_active=True).values('id', 'code', 'id_card', 'name', 'last_name1', 'last_name2', 'email', 'phone', 'category')
    return self.queryset 
  
  def create(self, request):
    user_serialized = self.serializer_class(data=request.data)
    if user_serialized.is_valid():
      user_serialized.save()
      return Response({'message': 'Usuario registrado correctamente'}, status=status.HTTP_201_CREATED)
    return Response({'message':'Error al registrar', 'errors': user_serialized.errors}, status=status.HTTP_400_BAD_REQUEST)
  
  def list(self, request):
    users = self.get_queryset()
    users_serialized = self.list_serializer_class(users, many=True)
    return Response(users_serialized.data, status=status.HTTP_200_OK)
  
  def retrieve(self, request, pk=None):
    user = get_object_or_404(self.model, pk=pk)
    user_serialized = self.serializer_class(user)
    return Response(user_serialized.data)
  
  def update(self, request, pk=None):
    user = get_object_or_404(self.model, pk=pk)
    user_serialized = UpdataUserSerializer(user, data=request.data)
    if user_serialized.is_valid():
      user_serialized.save()
      return Response({'message': 'Usuario actualizado correctamente'}, status=status.HTTP_200_OK)
    return Response({'message':'Error al actualizar', 'errors': user_serialized.errors}, status=status.HTTP_400_BAD_REQUEST)
  
  def destroy(self, request, pk=None):
    user_destroy = self.model.objects.filter(id=pk).update(is_active=False)
    if user_destroy == 1:
      return Response({
        'message': 'Usuario eliminado correctamente'
      })
    return Response({
      'message': 'No existe el usuario que desea eliminar'
    }, status=status.HTTP_404_NOT_FOUND)
    
