from django import template

register = template.Library()

@register.filter
def field_type(field, ftype):
    try:
        t = field.field.widget.__class__.__name__
        return t.lower() == ftype
    except:
        pass
    return False 

@register.simple_tag(takes_context=True)
def set_this_field_type(context, field):
    """
    Adds to context given field type variable
    variable named "this_field_type"
    """
    context["this_field_type"] = field.field.__class__.__name__
    return ''