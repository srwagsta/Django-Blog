from django.contrib.auth.mixins import PermissionRequiredMixin


class BlogPermissionsMixin(PermissionRequiredMixin):
    raise_exception = True
    permission_denied_message = 'Sorry, you do not have the permissions required to do this action.'

