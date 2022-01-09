from django.template.defaulttags import register


@register.filter(name='access')
def access(value, arg):
    try:
        result = value[arg] 
        return result
    except:
        return "" 