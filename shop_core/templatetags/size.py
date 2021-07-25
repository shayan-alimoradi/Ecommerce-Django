from hurry.filesize import size
from django import template

register = template.Library()


@register.filter
def convert(value):
	return size(value)