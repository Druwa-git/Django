from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('api/', views.PostListAPIView.as_view()),
    path('api/<uuid:pk>/', views.PostDetailAPIView.as_view()),
    path('api/<uuid:pk>/comments/', views.CommentListAPIView.as_view()),
    path('api/<uuid:post_pk>/comments/<int:pk>', views.CommentDetailAPIView.as_view()),
    path('', TemplateView.as_view(template_name='post/index.html'),name='list'),
    path('detail/', TemplateView.as_view(template_name='post/detail.html'),name='detail'),
    path('posting/', TemplateView.as_view(template_name='post/post.html'),name='post'),
]
