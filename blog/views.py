from django.views.generic import (ListView, TemplateView, DetailView,
                                  CreateView, UpdateView, DeleteView)
from django.urls import reverse_lazy
from .models import Post, Comment
from .forms import PostForm, CommentForm
from django.contrib.auth.mixins import LoginRequiredMixin
from rules.contrib.views import PermissionRequiredMixin
from django.contrib.auth import get_user_model


GENERIC_CRISPY_FORM_PATH = 'blog/forms/generic_crispy_form.html'
GENERIC_DELETE_TEMPLATE_PATH = 'blog/forms/generic_confirm_delete.html'
GENERIC_FAILED_DELETE_TEMPLATE_PATH = 'blog/forms/generic_failed_delete.html'
PERMISSION_DENIED_MESSAGE = 'Sorry, you do not have the permissions required to do this action.'


class BlogHomeView(TemplateView):
    template_name = 'blog/blog_home.html'

    def get_context_data(self, **kwargs):
        context = super(BlogHomeView, self).get_context_data(**kwargs)
        context['page_title'] = 'Crits and Coffee Blog'
        # Model Totals
        context['total_post_count'] = Post.objects.count()
        context['total_comment_count'] = Comment.objects.count()
        context['total_user_count'] = get_user_model().objects.count()
        # First users for the avatar pic and the first name field
        first_4_users = get_user_model().objects.all()[:4]
        context['first_user'] = first_4_users[0]
        context['user_profiles'] = first_4_users
        # 2 most recent posts to be pinned
        context['top_posts'] = Post.objects.all().order_by('-post_id')[:2]
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

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.post_author = self.request.user
        return super().form_valid(form)


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
