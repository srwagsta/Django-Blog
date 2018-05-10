from django.urls import path
from .views import (
    BlogHomeView,
    PostCreate, PostUpdate, PostDelete, PostListView, PostDetailView,
    CommentCreate, CommentUpdate, CommentDelete)

app_name = 'blog'
urlpatterns = [
    path('', BlogHomeView.as_view(), name='home'),
    path('post-create/', PostCreate.as_view(), name='post_create'),
    path('posts/<slug>/update/', PostUpdate.as_view(), name='post_update'),
    path('posts/<slug>/delete/', PostDelete.as_view(), name='post_delete'),
    path('posts/', PostListView.as_view(), name='post_list'),
    path('posts/<slug>/', PostDetailView.as_view(), name='post_detail'),
    path('posts/<post_id>/comment-create/', CommentCreate.as_view(), name='comment_create'),
    path('posts/<post_slug>/comments/<comment_slug>/update/', CommentUpdate.as_view(), name='comment_update'),
    path('posts/<post_slug>/comments/<slug>/delete/', CommentDelete.as_view(), name='comment_delete'),
]
