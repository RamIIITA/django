from djongo import models

class Blog(models.Model):
    name = models.CharField(max_length=100)
    title = models.TextField()
    text = models.TextField()

