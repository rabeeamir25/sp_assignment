from django.db import models
from django.contrib.auth.models import User
from blog.models.category import Category
from blog.managers.post_manager import PostManager

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category)
    likes = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, blank=True)  # Q8

    objects = PostManager()  # Q3 & Q4

    def __str__(self):
        return self.title
