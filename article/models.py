from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

# Create your models here.
class Article(models.Model):
    author = models.ForeignKey(get_user_model(), verbose_name="작성자", on_delete=models.CASCADE )
    title = models.CharField(max_length=50)
    content = models.TextField()