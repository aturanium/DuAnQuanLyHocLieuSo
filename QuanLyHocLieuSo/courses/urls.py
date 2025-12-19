from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('categories', views.CategoryViewSet)
router.register('courses', views.CourseViewSet)
router.register('lessons', views.LessonViewSet)
router.register('materials', views.MaterialViewSet)
router.register('users', views.UserViewSet)
router.register('comments', views.CommentViewSet)

urlpatterns = [
    path('', include(router.urls))
]