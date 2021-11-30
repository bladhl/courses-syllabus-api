from rest_framework import serializers
from apps.courses.models import CourseCategory, Course


class CourseCategorySerializer(serializers.ModelSerializer):
  class Meta:
    model = CourseCategory
    fields = '__all__'
    
class CourseSerializer(serializers.ModelSerializer):
  
  class Meta:
    model = Course
    fields = '__all__'
  
  def to_representation(self, instance):
    return {
      'id': instance.id,
      'name': instance.name,
      'credits': instance.credits,
      'category': instance.category.code,
      'professor': instance.professor.name
    }