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

class MaterialType(models.IntegerChoices):
    DOCUMENT = 1, 'Giáo trình'
    SLIDE = 2, 'Slide'
    VIDEO = 3, 'Video'
    REFERENCE = 4, 'Tham khảo'
    OTHER = 5, 'Khác'

class Level(models.IntegerChoices):
    BASIC = 1, 'Cơ bản'
    INTERMEDIATE = 2, 'Trung cấp'
    ADVANCED = 3, 'Nâng cao'

class Topic(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Material(BaseModel):
    name = models.CharField(max_length=255)
    file = CloudinaryField('file', resource_type='auto', folder='materials', null=True, blank=True, )
    description = models.TextField(null=True, blank=True)

    material_type = models.IntegerField(choices=MaterialType.choices, default=MaterialType.SLIDE)
    level = models.IntegerField( choices=Level.choices, default=Level.BASIC)
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, related_name='materials')
    uploaded_by = models.ForeignKey( User, on_delete=models.CASCADE, limit_choices_to={'role__in': [User.ADMIN, User.TEACHER]})
    topics = models.ManyToManyField(Topic,related_name='materials',blank=True)

    def __str__(self):
        return self.name


class Question(BaseModel):
    title = models.CharField(max_length=255)
    content = models.TextField()
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    is_solved = models.BooleanField(default=False)


class Answer(BaseModel):
    content = models.TextField()
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    is_accepted = models.BooleanField(default=False)


class Interaction(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True


class Comment(Interaction):
    content = models.TextField()
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True, blank=True, related_name='comments')
    material = models.ForeignKey(Material, on_delete=models.CASCADE, null=True, blank=True, related_name='comments')
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        target = self.material.name if self.material else (self.lesson.subject if self.lesson else "unknown")
        return f"{self.user.username} - {target}: {self.content[:30]}"


class Like(Interaction):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, null=True, blank=True, related_name='likes')
    material = models.ForeignKey(Material, on_delete=models.CASCADE, null=True, blank=True, related_name='likes')

    class Meta:
        unique_together = (('user', 'lesson'), ('user', 'material'))

    def __str__(self):
        target = self.material.name if self.material else (self.lesson.subject if self.lesson else "unknown")
        return f"{self.user.username} liked {target}"


class Note(Interaction):
    material = models.ForeignKey(Material, on_delete=models.CASCADE, related_name='notes')
    content = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"Note by {self.user.username} on {self.material.name}"