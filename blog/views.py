from django.views.generic import (ListView, TemplateView, DetailView,
                                  CreateView, UpdateView, DeleteView)
from django.urls import reverse_lazy
from .models import Post, Comment


class PostListView(ListView):
    model = Post
    context_object_name = 'post_list'
    paginate_by = 5
    queryset = Post.objects.all()


class PostDetailView(DetailView):
    model = Post


class CommentDetailView(DetailView):
    model = Comment
