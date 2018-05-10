from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.contrib.auth.models import Group


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def add_to_default_group(sender, **kwargs):
    user = kwargs['instance']
    if kwargs['created']:
        try:
            group = Group.objects.get(name='default')
            user.groups.add(group)
        except:
            group = Group.objects.create(name='default')
            user.groups.add(group)
