from django.contrib import admin

from apps.courses.models import CourseCategory, Course


# Register your models here.
admin.site.register(CourseCategory)
admin.site.register(Course)