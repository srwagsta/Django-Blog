from django.views.generic import (ListView, TemplateView, DetailView,
                                  CreateView, UpdateView, DeleteView)
from django.urls import reverse_lazy
from .models import Post, Comment
from .forms import PostForm, CommentForm
from .mixins import BlogPermissionsMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.shortcuts import get_object_or_404


GENERIC_CRISPY_FORM_PATH = 'blog/forms/generic_crispy_form.html'
GENERIC_DELETE_TEMPLATE_PATH = 'blog/forms/generic_confirm_delete.html'
GENERIC_FAILED_DELETE_TEMPLATE_PATH = 'blog/forms/generic_failed_delete.html'


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
        if len(first_4_users) > 0:
            context['first_user'] = first_4_users[0]
        context['user_profiles'] = first_4_users
        # 2 most recent posts to be pinned
        context['top_posts'] = Post.objects.all().order_by('-post_id')[:2]
        return context


class PostCreate(LoginRequiredMixin, CreateView):
    model = Post
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


class PostUpdate(BlogPermissionsMixin, LoginRequiredMixin, UpdateView):
    model = Post
    permission_required = 'blog.can_edit_post'
    success_msg = "Post Updated!"
    form_class = PostForm
    template_name = GENERIC_CRISPY_FORM_PATH

    def get_context_data(self, **kwargs):
        context = super(PostUpdate, self).get_context_data(**kwargs)
        context['page_title'] = 'Update Post'
        return context


class PostDelete(BlogPermissionsMixin, LoginRequiredMixin, DeleteView):
    model = Post
    permission_required = 'blog.can_delete_post'
    success_url = reverse_lazy('blog:post_list')
    template_name = GENERIC_DELETE_TEMPLATE_PATH
    failed_delete_template = GENERIC_FAILED_DELETE_TEMPLATE_PATH


class PostListView(ListView):
    model = Post
    context_object_name = 'post_list'
    paginate_by = 5

    def get_queryset(self):
        search_name = self.request.GET.get('name', '')
        if search_name != '':
            return self.model.objects.filter(post_author__first_name=search_name)
        else:
            return self.model.objects.all()


class PostDetailView(DetailView):
    model = Post


# Start Comment Views
class CommentCreate(LoginRequiredMixin, CreateView):
    model = Comment
    success_msg = "Comment Published!"
    form_class = CommentForm
    template_name = GENERIC_CRISPY_FORM_PATH

    def get_success_url(self, **kwargs):
        return reverse_lazy('blog:post_detail', args=(self.object.post.slug,))

    def get_form(self):
        form = super(CommentCreate, self).get_form()
        post = get_object_or_404(Post, pk=self.kwargs['post_id'])
        form.instance.post = post
        return form

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.comment_author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(CommentCreate, self).get_context_data(**kwargs)
        context['page_title'] = 'Create Comment'
        return context


class CommentUpdate(BlogPermissionsMixin, LoginRequiredMixin, UpdateView):
    model = Comment
    permission_required = 'blog.can_edit_comment'
    success_msg = "Comment Updated!"
    form_class = CommentForm
    template_name = GENERIC_CRISPY_FORM_PATH

    def get_context_data(self, **kwargs):
        context = super(CommentUpdate, self).get_context_data(**kwargs)
        context['page_title'] = 'Update Comment'
        return context


class CommentDelete(BlogPermissionsMixin, LoginRequiredMixin, DeleteView):
    model = Comment
    permission_required = 'blog.can_delete_comment'
    success_url = reverse_lazy('blog:post_list')
    template_name = GENERIC_DELETE_TEMPLATE_PATH
    failed_delete_template = GENERIC_FAILED_DELETE_TEMPLATE_PATH
