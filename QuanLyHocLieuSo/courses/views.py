from rest_framework import viewsets, generics, parsers, permissions
from .models import Category, Course, Lesson, Material, User, Comment
from .serializers import CategorySerializer, CourseSerializer, LessonSerializer, MaterialSerializer, UserSerializer, CommentSerializer

class UserViewSet(viewsets.ViewSet, generics.CreateAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer
    parser_classes = [parsers.MultiPartParser, ]

    def get_permissions(self):
        if self.action in ['retrieve']:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]
    
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.filter(active=True)
    serializer_class = CategorySerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.filter(active=True)
    serializer_class = CourseSerializer

    def get_queryset(self):
        queries = self.queryset
        q = self.request.query_params.get("q")
        if q:
            queries = queries.filter(subject__icontains=q)
        return queries
    
class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.filter(active=True)
    serializer_class = LessonSerializer

class MaterialViewSet(viewsets.ModelViewSet):
    queryset = Material.objects.filter(active=True)
    serializer_class = MaterialSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.filter(active=True)
    serializer_class = CommentSerializer

    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
