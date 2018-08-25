from django import template
register=template.Library()
@register.filter(name='times') 
def times(number):
    return range(number)

@register.filter(name='index')
def index(List, i):
    return List[int(i)]