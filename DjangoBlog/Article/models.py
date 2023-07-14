from django.db import models
from django.contrib.auth.models import User


class Article(models.Model):
    title = models.CharField(max_length=200)
    desc = models.TextField()
    slug = models.SlugField(max_length=100, unique=True)
    published = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE) #(Cascade)remove all articles of author when author is deleted
    
    def __str__(self) -> str:
        return self.title