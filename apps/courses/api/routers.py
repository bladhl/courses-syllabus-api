from rest_framework.routers import DefaultRouter
from apps.courses.api.views import CourseViewSet, CourseCategoryViewSet

router = DefaultRouter()
router.register('', CourseViewSet, basename='courses')

urlpatterns = router.urls