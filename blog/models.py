from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from django.utils.text import slugify
import itertools


class Post(models.Model):
    post_id = models.IntegerField(primary_key=True)
    post_title = models.CharField(max_length=75, unique=True)
    post_author = models.ForeignKey(User, related_name='posts', on_delete=models.CASCADE)
    post_content = models.TextField()
    publish_date = models.DateTimeField(editable=False)
    edit_date = models.DateTimeField()
    slug = models.SlugField(unique=True, editable=False)

    def __str__(self):
        return '%s: %s' % (self.post_title, self.post_author)

    def get_absolute_url(self):
        return reverse('blog:post_detail', kwargs={'slug': self.slug})

    def _get_unique_slug(self):
        unique_slug = slugify(self)
        for x in itertools.count(1):
            if not Post.objects.filter(slug=unique_slug).exists():
                break
            unique_slug = '%s-%d' % (unique_slug, x)
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        if not self.post_id:
            self.publish_date = timezone.now()
        self.edit_date = timezone.now()
        return super(Post, self).save(*args, **kwargs)

    class Meta:
        ordering = ['publish_date', 'edit_date', 'post_author']


class Comment(models.Model):
    comment_id = models.IntegerField(primary_key=True)
    post = models.OneToOneField(Post, on_delete=models.CASCADE)
    comment_content = models.TextField()
    comment_author = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    publish_date = models.DateTimeField()
    edit_date = models.DateTimeField()
    slug = models.SlugField()
    likes = models.IntegerField(default=0)

    def __str__(self):
        return '%s: %s: %s' % (self.comment_author, self.publish_date, self.post.post_title)

    def get_absolute_url(self):
        return reverse('blog:comment_detail', kwargs={'slug': self.slug})

    def _get_unique_slug(self):
        unique_slug = slugify(self)
        for x in itertools.count(1):
            if not Post.objects.filter(slug=unique_slug).exists():
                break
            unique_slug = '%s-%d' % (unique_slug, x)
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        if not self.comment_id:
            self.publish_date = timezone.now()
        self.edit_date = timezone.now()
        return super(Comment, self).save(*args, **kwargs)

    class Meta:
        ordering = ['likes', 'publish_date', 'edit_date', 'post_author']
