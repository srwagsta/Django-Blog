from django.views.generic import (ListView, TemplateView, DetailView,
                                  CreateView, UpdateView, DeleteView)
from django.urls import reverse_lazy
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin


GENERIC_CRISPY_FORM_PATH = 'blog/forms/generic_crispy_form.html'
GENERIC_DELETE_TEMPLATE_PATH = 'blog/forms/generic_confirm_delete.html'
GENERIC_FAILED_DELETE_TEMPLATE_PATH = 'blog/forms/generic_failed_delete.html'
PERMISSION_DENIED_MESSAGE = 'Sorry, you do not have the permissions required to do this action.'


class BlogHomeView(TemplateView):
    template_name = 'blog/blog_home.html'

    def get_context_data(self, **kwargs):
        # TODO: Add any context data needed here (number of posts, comments, top posts, most liked .... etc
        context = super(BlogHomeView, self).get_context_data(**kwargs)
        context['page_title'] = 'Crits and Coffee Blog'
        return context


class PostCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Post
    permission_required = 'post.can_publish_post'
    permission_denied_message = PERMISSION_DENIED_MESSAGE
    success_msg = "Post Published!"
    form_class = PostForm
    template_name = GENERIC_CRISPY_FORM_PATH

    def get_context_data(self, **kwargs):
        context = super(PostCreate, self).get_context_data(**kwargs)
        context['page_title'] = 'Create Post'
        return context


# TODO: Make sure that the user editing the post matches the author
class PostUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Post
    permission_required = 'post.can_edit_post'
    permission_denied_message = PERMISSION_DENIED_MESSAGE
    success_msg = "Post Updated!"
    form_class = PostForm
    template_name = GENERIC_CRISPY_FORM_PATH

    def get_context_data(self, **kwargs):
        context = super(PostUpdate, self).get_context_data(**kwargs)
        context['page_title'] = 'Update Post'
        return context


# TODO: Make sure the the user deleting the post is an admin or the author
class PostDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Post
    permission_required = 'post.can_delete_post'
    permission_denied_message = PERMISSION_DENIED_MESSAGE
    success_url = reverse_lazy('blog:post_list')
    template_name = GENERIC_DELETE_TEMPLATE_PATH
    failed_delete_template = GENERIC_FAILED_DELETE_TEMPLATE_PATH


class PostListView(ListView):
    model = Post
    context_object_name = 'post_list'
    paginate_by = 5
    queryset = Post.objects.all()


class PostDetailView(DetailView):
    model = Post


# Start Comment Views
class CommentCreate(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Comment
    permission_required = 'comment.can_create_comment'
    permission_denied_message = PERMISSION_DENIED_MESSAGE
    success_msg = "Comment Published!"
    form_class = CommentForm
    template_name = GENERIC_CRISPY_FORM_PATH

    def get_context_data(self, **kwargs):
        context = super(CommentCreate, self).get_context_data(**kwargs)
        context['page_title'] = 'Create Comment'
        return context


# TODO: Make sure that the user editing the comment matches the author
class CommentUpdate(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Comment
    permission_required = 'comment.can_edit_comment'
    permission_denied_message = PERMISSION_DENIED_MESSAGE
    success_msg = "Comment Updated!"
    form_class = CommentForm
    template_name = GENERIC_CRISPY_FORM_PATH

    def get_context_data(self, **kwargs):
        context = super(CommentUpdate, self).get_context_data(**kwargs)
        context['page_title'] = 'Update Comment'
        return context


# TODO: Make sure the the user deleting the comment is an admin or the author
class CommentDelete(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Comment
    permission_required = 'comment.can_delete_comment'
    permission_denied_message = PERMISSION_DENIED_MESSAGE
    success_url = reverse_lazy('blog:comment_list')
    template_name = GENERIC_DELETE_TEMPLATE_PATH
    failed_delete_template = GENERIC_FAILED_DELETE_TEMPLATE_PATH


class CommentListView(ListView):
    model = Comment
    context_object_name = 'comment_list'
    paginate_by = 5
    queryset = Comment.objects.all()


class CommentDetailView(DetailView):
    model = Comment
