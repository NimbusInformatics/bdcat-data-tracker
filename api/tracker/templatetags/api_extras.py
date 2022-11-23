from django import template
from django.template.defaultfilters import stringfilter


register = template.Library()


@register.filter
@stringfilter
def uncapitalize(value):
    if value is None or len(value) == 0:
        return value

    return value[0].lower() + value[1:]


@register.filter
def istoastmessage(message):
    return (
            hasattr(message, 'extra_tags')
            and 'toast' in str(message.extra_tags)
    )


def _toasttype(message):
    tags = message.extra_tags.split(' ')
    toast_tag = next(tag for tag in tags if 'toast-' in tag)

    return toast_tag.split('-')[1]


@register.filter
def toastbgcolor(message):
    if _toasttype(message) == 'error':
        return 'danger'

    return 'light'


@register.filter
def toasttxtcolor(message):
    if _toasttype(message) == 'error':
        return 'light'

    return 'dark'
