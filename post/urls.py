from django.urls import path
from . import views

urlpatterns = [
    path('post/', views.PostListAPIView.as_view()),
    path('post/<pk>/', views.PostDetailAPIView.as_view()),
]
