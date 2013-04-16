from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def add_braces(value):
    return "{"+value+"}"

@register.filter
@stringfilter
def double_stache(value):
    return "{{"+value+"}}"
