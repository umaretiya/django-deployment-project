from atexit import register
from django import template

register = template.Library()

@register.filter(name='cut') #used decorators instead of calling function
def cut(value,args):
    """
    This cuts our all values of "arg" form the string!
    """
    return value.replace(args,'')

#register.filter('cut',cut) 