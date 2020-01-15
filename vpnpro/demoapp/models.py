
from django.db import models 
class Blog(models.Model):
    author = models.CharField(max_length=100)
    title = models.TextField()
    text = models.TextField()
