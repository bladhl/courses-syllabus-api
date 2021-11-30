from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.parsers import JSONParser, MultiPartParser


from apps.courses.models import CourseCategory, Course
from apps.courses.api.serializers import CourseSerializer, CourseCategorySerializer

class CourseCategoryViewSet(viewsets.ModelViewSet):
  model = CourseCategory
  serializer_class = CourseCategorySerializer

  def get_queryset(self):
    return self.get_serializer().Meta.model.objects.all()

  def list(self, request):
    data = self.get_queryset()
    data = self.get_serializer(data, many=True)
    return Response(data.data)
  

class CourseViewSet(viewsets.ModelViewSet):
  model = Course
  serializer_class = CourseSerializer
  
  def get_queryset(self, pk=None):
    if pk is None:
      return self.get_serializer().Meta.model.objects.all()
    return self.get_serializer().Meta.model.objects.filter(id=pk).first()

  def list(self, request):
    course_serialized = self.serializer_class(self.get_queryset(), many=True)
    return Response(course_serialized.data, status=status.HTTP_200_OK)
    