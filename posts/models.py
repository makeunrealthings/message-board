# posts/models.py
from django.db import models
class Post(models.Model):
    text = models.TextField()
    def __str__(self): # new
      return self.text[:50]