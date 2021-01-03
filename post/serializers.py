from rest_framework import serializers
from .models import Post, Comment
#from django.contrib.auth.models import User

class PostSerializer(serializers.ModelSerializer):
	author = serializers.CharField()
	created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
	edited_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
	class Meta:
		model = Post
		fields = ('uid','title','author','content','created_at','edited_at')


class CommentSerializer(serializers.ModelSerializer):
	author = serializers.CharField()
	created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")
	class Meta:
		model = Comment
		fields = ('id', 'post', 'author', 'content', 'created_at')
