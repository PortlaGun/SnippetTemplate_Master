from django.contrib.auth.models import User
from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'


class Snippet(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, unique=False, blank=False, null=True)
    name = models.CharField(max_length=100, unique=False, blank=False, null=False)
    lang = models.CharField(max_length=30, unique=False, blank=False, null=False)
    code = models.TextField(max_length=5000, unique=False, blank=False, null=False)
    hide = models.BooleanField(default=False, unique=False, blank=False, null=False)
    is_public = models.BooleanField(default=False, unique=False, blank=False, null=False)
    creation_date = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    text = models.TextField(max_length=1000, unique=False, blank=False, null=False)
    creation_date = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, unique=False, blank=False, null=True)
    snippet = models.ForeignKey(Snippet, on_delete=models.CASCADE, unique=False, blank=False, null=True)
