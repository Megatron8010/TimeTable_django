from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=30)
    director = models.CharField(max_length=30)
    ratings = models.CharField(max_length=30,default="")
    imdb_link = models.CharField(max_length=30,default="")
    cast = models.CharField(max_length=30,default="")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="movie", null=True)

class TableUser(models.Model):
    username = models.TextField(default="none")
    json_data = models.TextField()