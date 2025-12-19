from django.contrib import admin
from .models import Category, Course, Lesson, Material, User, Comment, Like

admin.site.register(Category)
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Material)
admin.site.register(User)
admin.site.register(Comment)
admin.site.register(Like)