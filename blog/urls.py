from django.urls import path
from .views import (
    PostListView,
    PostDetailView, CommentDetailView)

app_name = 'blog'
urlpatterns = [
    path('', PostListView),
    path('posts/', PostListView),
    path('posts/<slug>/', PostDetailView),
    path('posts/<slug>/comments/<slug>', CommentDetailView),
]
