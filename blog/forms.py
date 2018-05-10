from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Post, Comment


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['post_title', 'post_content']

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'register__form'
        self.helper.add_input(Submit('submit', 'Publish Post'))

    def clean_post_title(self):
        return self.cleaned_data['post_title'].strip()


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment_content']

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'register__form'
        self.helper.add_input(Submit('submit', 'Submit Comment'))

    def clean_post_title(self):
        return self.cleaned_data['comment_content'].strip()
