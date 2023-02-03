from django.urls import path, re_path

from views import course

from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('category', course.CourseCategoryView)
router.register('', course.CourseView)

urlpatterns = [

]

urlpatterns += router.urls
