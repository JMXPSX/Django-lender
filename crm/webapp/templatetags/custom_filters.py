from django import template

register = template.Library()

@register.filter
def add_asterisk(field):
    if field.field.required:
        return f'{field.label} <span class="text-red-500">*</span>'
    return field.label
