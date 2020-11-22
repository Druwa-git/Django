from rest_framework import serializers
from .models import Post, Comment
#from django.contrib.auth.models import User

class PostSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		#author = author.get_full_name()
		fields = ('uid','title','author','content','created_at','edited_at')


class CommentSerializer(serializers.ModelSerializer):
	class Meta:
		model = Comment
		fields = ('post', 'author', 'content', 'created_at')