from django import template

register = template.Library()

# @register.filter
# def add_class(field, css_class):
#     return f'<div class="{css_class}">{field}</div>'

# from django import template

# register = template.Library()

@register.filter
def add_class(field, css_class):
    attrs = field.attrs
    attrs['class'] = css_class
    return field