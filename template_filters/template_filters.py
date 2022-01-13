from django.template.defaulttags import register


@register.filter(name='access')
def access(value, arg):
    try:
        result = value[arg] 
        return result
    except:
        return "" 
@register.filter(name='lookupMIN')
def lookupMIN(value, arg):
    return value.get(arg)[0]

@register.filter(name='lookupMAX')
def lookupMAX(value, arg):
    return value.get(arg)[1]

@register.filter(name='access2')
def access2(value, arg):
    return value[arg][0]

@register.filter(name='adress')
def adress(value):
    return value[2:-1]

@register.filter(name='return_template')
def return_template(value):
    return value[:-1]