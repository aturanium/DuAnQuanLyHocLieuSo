from rest_framework import viewsets, generics, parsers, permissions
from rest_framework.permissions import IsAuthenticated
from django.db.models import  Q
from rest_framework.response import Response

from .models import Category, Course, Lesson, Material, User, Comment, Topic, Like, Note
from .serializers import CategorySerializer, CourseSerializer, LessonSerializer, MaterialSerializer, UserSerializer, \
    CommentSerializer, TopicSerializer, NoteSerializer, LikeSerializer


class UserViewSet(viewsets.ViewSet, generics.CreateAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = UserSerializer
    parser_classes = [parsers.MultiPartParser, ]

    def get_permissions(self):
        if self.action in ['retrieve']:
            return [permissions.IsAuthenticated()]
        return [permissions.AllowAny()]

    def list(self, request, *args, **kwargs):

        q = request.query_params.get('q')
        qs = self.queryset
        if q:
            if q.isdigit():
                qs = qs.filter(id=int(q))
            else:
                qs = qs.filter(Q(first_name__icontains=q) | Q(last_name__icontains=q))
        serializer = UserSerializer(qs, many=True, context={'request': request})
        return Response(serializer.data)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.filter(active=True)
    serializer_class = CategorySerializer


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.filter(active=True)
    serializer_class = CourseSerializer

    def get_queryset(self):
        queries = self.queryset
        q = self.request.query_params.get("q")
        category= self.request.query_params.get("category")

        if category:
            queries = queries.filter(category_id=category)

        if q:
            queries = queries.filter(subject__icontains=q)

        return queries


class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.filter(active=True)
    serializer_class = LessonSerializer


class TopicViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Topic.objects.filter(active=True)
    serializer_class = TopicSerializer



class MaterialViewSet(viewsets.ModelViewSet):
    serializer_class = MaterialSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = Material.objects.filter(active=True)

        q = self.request.query_params.get('q')
        lesson = self.request.query_params.get('lesson')
        topic = self.request.query_params.get('topic')
        material_type = self.request.query_params.get('material_type')
        level = self.request.query_params.get('level')

        if q:
            queryset = queryset.filter(
                Q(name__icontains=q) |
                Q(description__icontains=q) |
                Q(lesson__subject__icontains=q)
            )

        if lesson:
            queryset = queryset.filter(lesson_id=lesson)

        if topic:
            queryset = queryset.filter(topics__id=topic)

        if material_type:
            queryset = queryset.filter(material_type=material_type)

        if level:
            queryset = queryset.filter(level=level)

        return queryset.distinct()

    def perform_create(self, serializer):
        serializer.save(uploaded_by=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.filter(active=True)
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.filter(material__isnull=False)
    serializer_class = NoteSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)