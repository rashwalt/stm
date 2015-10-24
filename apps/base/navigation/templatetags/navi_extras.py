from django import template

from apps.base.navigation.enums import Navigation

register = template.Library()


@register.inclusion_tag('apps/base/navigation.html')
def navigation(page_id):
    return {
        'page_id': page_id,
        'navigation': list(Navigation),
    }
