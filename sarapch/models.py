from django.db import models

# Create your models here.
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    photo = models.ImageField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title