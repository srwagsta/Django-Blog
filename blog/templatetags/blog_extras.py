from django import template

register = template.Library()


@register.filter('in_group')
def in_group(user, group_name):
    groups = user.groups.all().values_list('name', flat=True)
    return True if group_name in groups else False
