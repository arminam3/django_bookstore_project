from django import template

register =template.Library()

@register.filter
def my_lower(value, arg):
    return f'{value[0:int(arg):].upper()}{value[int(arg)::]}'
