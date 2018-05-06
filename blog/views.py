from django.views.generic import (ListView, TemplateView, DetailView,
                                  CreateView, UpdateView, DeleteView)
from django.urls import reverse_lazy
from .models import Post, Comment


class BlogHomeView(TemplateView):
    template_name = 'blog/blog_home.html'


class PostCreate(CreateView):
    model = Post
    success_msg = "Post Published!"
    form_class = PostForm
    template_name = GENERIC_CRISPY_FORM_PATH

    def get_context_data(self, **kwargs):
        context = super(PostCreate, self).get_context_data(**kwargs)
        context['page_title'] = 'Create Post'
        return context


class PostListView(ListView):
    model = Post
    context_object_name = 'post_list'
    paginate_by = 5
    queryset = Post.objects.all()


class PostDetailView(DetailView):
    model = Post


class CommentDetailView(DetailView):
    model = Comment
