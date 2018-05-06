from django.urls import path
from .views import (
    BlogHomeView,
    PostCreate, PostListView,
    PostDetailView, CommentDetailView)

app_name = 'blog'
urlpatterns = [
    path('', BlogHomeView.as_view(), name='home'),
    path('post-create', PostCreate.as_view(), name='post_create')
    path('posts/', PostListView.as_view(), name='post_list'),
    path('posts/<slug>/', PostDetailView.as_view(), name='post_detail'),
    path('posts/<slug>/comments/<slug2>', CommentDetailView.as_view(), name='post_comments'),
    # TODO: Add post_update, post delete, and comment_create urls
]
