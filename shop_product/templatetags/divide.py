from django import template


register = template.Library()


@register.filter(name='div')
def divide(value, arg):
    try:
        return int(value) / int(arg)
    except (ValueError, ZeroDivisionError):
        return None