import ipdb
from django import template
import datetime

register = template.Library()

def mylower(string):
    return "whatup?"

register.filter('mylower',mylower)

@register.tag("say_hi")
def do_format_time(parser, token):
    try:
        tag_name, error_list = token.split_contents()
    except ValueError:
        raise template.TemplateSyntaxError("%r tag requires exactly two arguments" % token.contents.split()[0])
    return ErrorNode(error_list)

class ErrorNode(template.Node):
    def __init__(self, error_list):
        self.error_list = template.Variable(error_list)

    def render(self, context):
        try:
            actual_error_list = [str(error) for error in self.error_list.resolve(context)]
            return ",".join(actual_error_list)
        except template.VariableDoesNotExist:
            return ''

@register.inclusion_tag('error_list.html')
def error_div(error_list):
    return {'error_list': error_list}

@register.inclusion_tag('form_errors.html')
def all_errors(form):
    return {'form':form} 
