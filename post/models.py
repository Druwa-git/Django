import uuid

from django.conf import settings
from django.db import models

# Create your models here.


class Post(models.Model):
    def created_author(self):
        return self.author.first_name;

    def created_time(self):
        time = self.created_at;
        return time.year + "년" + time.month + "월" + time.day + "일" + time.hour + "시" + time.minute + "분";

    uid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True, primary_key=True)
    title = models.CharField(max_length=100)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='authors')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    post = models.ForeignKey('Post',on_delete=models.CASCADE,related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
