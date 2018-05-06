from django.urls import path
from .views import (
    BlogHomeView,
    PostListView,
    PostDetailView, CommentDetailView)

app_name = 'blog'
urlpatterns = [
    path('', BlogHomeView.as_view(), name='home'),
    path('posts/', PostListView.as_view(), name='post_list'),
    path('posts/<slug>/', PostDetailView.as_view(), name='post_detail'),
    path('posts/<slug>/comments/<slug2>', CommentDetailView.as_view(), name='post_comments'),
]
