from django.db import models
from django.contrib.auth.models import User

# Create your models here.

STATUS = {(0, 'Draft'), (1, 'Publish')}


# Created a model for Post
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(to=User, on_delete=models.CASCADE)
    status = models.IntegerField(choices=STATUS, default=0)

    def __str__(self) -> str:
        return self.title
