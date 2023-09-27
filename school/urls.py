from school.apps import SchoolConfig
from rest_framework.routers import DefaultRouter

from school.views import CourseViewSet

app_name = SchoolConfig.name

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')


urlpatterns = [

              ] + router.urls
