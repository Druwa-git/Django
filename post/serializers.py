
from rest_framework import serializers
from .models import Post

class PostSerializer(serializers.ModelSerializer):
	class Meta:
		model = Post
		fields = ('uid','title','author','content','created_at','edited_at')