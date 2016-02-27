from django import template

register = template.Library()

@register.filter(name='minus')
def minus(value, arg):
    return value - arg
