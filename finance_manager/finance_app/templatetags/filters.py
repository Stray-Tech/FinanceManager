from django import template

register = template.Library()

# @register.filter
# def add_class(field, css_class):
#     return f'<div class="{css_class}">{field}</div>'

# from django import template

# register = template.Library()

@register.filter(name="add_class")
def add_class(css_class):
    # wrapperClass = field.attrs.data.wrapperClass
    return css_class