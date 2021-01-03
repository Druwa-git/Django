from django.shortcuts import render, get_object_or_404

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

# Authentication
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

# TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token


class PostListAPIView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        serializer = PostSerializer(Post.objects.all(), many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data;
        post = Post.objects.create(title=data['title'], content=data['content'], author=request.user)
        serializer = PostSerializer(data=request.data)
        serializer.is_valid()
        return Response(serializer.data, status=201)

class PostDetailAPIView(APIView):
    def get_object(self, pk):
        return get_object_or_404(Post, pk=pk)

    def get(self, request, pk, format=None):
        post = self.get_object(pk)
        serializer = PostSerializer(post)
        return Response(serializer.data)

    def put(self, request, pk):
        post = self.get_object(pk)
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        post = self.get_object(pk)
        post.delete()
        return Response(status=200)


class CommentListAPIView(APIView):
    #authentication_classes = [SessionAuthentication, BasicAuthentication]
    #permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        return get_object_or_404(Post, pk=pk)

    def get(self, request, pk, fomat=None):
        post = self.get_object(pk)
        serializer = CommentSerializer(post.comments.all(), many=True)
        return Response(serializer.data)

    def post(self, request, pk):
        post = self.get_object(pk)
        data = request.data
        post = Comment.objects.create(post=post, content=data['content'], author=request.user)
        serializer = CommentSerializer(data=request.data)
        #serializer.is_valid(raise_exception=True) This occur error 400 why?
        serializer.is_valid()
        #serializer.save() //accur 500 error
        return Response(serializer.data, status=201)

class CommentDetailAPIView(APIView):
    def get_comment(self, pk):
        return get_object_or_404(Comment, pk=pk)

    def get_object(self, post_pk):
        return get_object_or_404(Post, pk=post_pk)

    def get(self, request, pk, post_pk, format=None):
        comment = self.get_comment(pk)
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def put(self, request, pk, post_pk):
        post = self.get_object(post_pk)
        data = request.data
        Comment.objects.create(post=post, content=data['content'], author=request.user)
        serializer = CommentSerializer(data=request.data)
        serializer.is_valid()
        return Response(serializer.data, status=201)

    def delete(self, request, pk):
        comment = self.get_comment(pk)
        comment.delete()
        return Response(status=200)

"""
class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
        })
"""
