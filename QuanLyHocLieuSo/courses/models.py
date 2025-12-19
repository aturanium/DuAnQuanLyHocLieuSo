from django.db import models
from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField

class User(AbstractUser):
    avatar = CloudinaryField('avatar', folder='users', null=True, blank=True)

    ADMIN = 1
    TEACHER = 2
    STUDENT = 3
    ROLE_CHOICES = (
        (ADMIN, 'Administrator'),
        (TEACHER, 'Giảng viên'),
        (STUDENT, 'Sinh viên')
    )
    role = models.IntegerField(choices=ROLE_CHOICES, default=STUDENT)

class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True

class Category(BaseModel):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    
class Course(BaseModel):
    subject = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    image = CloudinaryField('image', folder='courses', null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT, related_name='courses')
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role': 2})

    def __str__(self):
        return self.subject

class Lesson(BaseModel):
    subject = models.CharField(max_length=255)
    content = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='lessons')

    def __str__(self):
        return self.subject

class Material(BaseModel):
    name = models.CharField(max_length=255)
    file_upload = CloudinaryField('file_upload', resource_type='auto', folder='materials')
    description = models.TextField(null=True, blank=True)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='materials')

    def __str__(self):
        return self.name
    
class Interaction(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)

    class Meta:
        abstract = True

class Comment(Interaction):
    content = models.TextField()

    def __str__(self):
        return f"{self.user.username} - {self.content}"
    
class Like(Interaction):
    class Meta:
        unique_together = ('user', 'lesson')

    def __str__(self):
        return f"{self.user.username} liked {self.lesson.subject}"