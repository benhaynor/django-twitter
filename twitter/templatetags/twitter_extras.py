import ipdb
from django import template
import datetime

register = template.Library()

@register.tag("say_hi")
def do_format_time(parser, token):
    try:
        tag_name, error_list = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError("%r tag requires exactly two arguments" % token.contents.split()[0])
    return ErrorNode(error_list)

@register.inclusion_tag('resources/error_list.html')
def error_div(error_list):
    return {'error_list': error_list}

@register.inclusion_tag('resources/form_errors.html')
def all_errors(form):
    return {'form':form}
