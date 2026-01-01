from rest_framework import serializers
from .models import Category, Course, Lesson, Material, User, Comment, Topic, Like, Note, Question, Answer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'username', 'avatar', 'role']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
            data = validated_data.copy()
            user = User(**data)
            user.set_password(user.password)
            user.save()
            return user
        
    def to_representation(self, instance):
            rep = super().to_representation(instance)
            if instance.avatar:
                rep['avatar'] = instance.avatar.url
            return rep

    def get_name(self, obj):
        full = f"{obj.first_name} {obj.last_name}".strip()
        return full if full else obj.username

        
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class CourseSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = ['id', 'subject', 'description', 'created_date', 'image', 'category', 'teacher']

    def get_image(self, course):
        if course.image:
            return course.image.url
        return None


class LessonSerializer(serializers.ModelSerializer):
    course = CourseSerializer()

    class Meta:
        model = Lesson
        fields = ['id', 'subject', 'content', 'created_date', 'course']


class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['id', 'name']


class MaterialSerializer(serializers.ModelSerializer):
    file = serializers.SerializerMethodField()
    uploaded_by = serializers.CharField(source='uploaded_by.username', read_only=True)
    lesson = LessonSerializer(read_only=True)
    topics = TopicSerializer(many=True, read_only=True)

    class Meta:
        model = Material
        fields = ['id', 'name', 'description', 'file', 'material_type', 'level', 'lesson', 'topics','uploaded_by', 'created_date' ]

    def get_file(self, obj):
        return obj.file.url if obj.file else None


class QuestionSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)
    answer_count = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = [ 'id', 'title', 'content','lesson', 'created_by','is_solved', 'created_date', 'answer_count']

    def get_answer_count(self, obj):
        return obj.answer_set.count()


class AnswerSerializer(serializers.ModelSerializer):
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Answer
        fields = ['id', 'content', 'question', 'created_by', 'is_accepted', 'created_date']


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'content', 'created_date', 'user', 'lesson', 'material', 'question', 'answer',]
        extra_kwargs = {
            'lesson': {'write_only': True}
        }


class LikeSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Like
        fields = ('id', 'user', 'lesson', 'material', 'created_date')


class NoteSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Note
        fields = ('id', 'user', 'material', 'content', 'created_date')