from django.forms import ModelForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Post, Comment


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['post_title']

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'Publish Post'))

    def clean_post_title(self):
        return self.cleaned_data['post_title'].strip()


class CommentForm(ModelForm):
    pass
