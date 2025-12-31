from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('categories', views.CategoryViewSet)
router.register('courses', views.CourseViewSet)
router.register('lessons', views.LessonViewSet)
router.register('topics', views.TopicViewSet)
router.register(r'materials', views.MaterialViewSet, basename='material')
router.register('users', views.UserViewSet)
router.register('comments', views.CommentViewSet)
router.register('likes', views.LikeViewSet)
router.register('notes', views.NoteViewSet)


urlpatterns = [
    path('', include(router.urls))
]