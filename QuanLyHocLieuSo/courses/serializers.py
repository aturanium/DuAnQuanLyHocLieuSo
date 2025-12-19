from rest_framework import serializers
from .models import Category, Course, Lesson, Material, User, Comment

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'username', 'password', 'avatar', 'role']
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
    image = serializers.SerializerMethodField()

    class Meta:
        model = Lesson
        fields = ['id', 'subject', 'content', 'created_date', 'course', 'image']

    def get_image(self, lesson):
        if lesson.image:
            return lesson.image.url
        return None
    
class MaterialSerializer(serializers.ModelSerializer):
    file_upload = serializers.SerializerMethodField()

    class Meta:
        model = Material
        fields = ['id', 'name', 'file_upload', 'description']

    def get_file_upload(self, material):
        if material.file_upload:
            return material.file_upload.url
        return None
    
class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'content', 'created_date', 'upload_date', 'user', 'lesson']
