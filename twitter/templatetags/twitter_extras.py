from django import template
import datetime

register = template.Library()

@register.inclusion_tag('resources/error_list.html')
def error_div(error_list):
    return {'error_list': error_list}

@register.inclusion_tag('resources/form_errors.html')
def all_errors(form):
    return {'form':form}
