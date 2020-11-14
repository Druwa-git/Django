from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostListAPIView.as_view()),
    path('<pk>/', views.PostDetailAPIView.as_view()),
    path('<pk>/comments', views.CommentListAPIView.as_view()),
]
