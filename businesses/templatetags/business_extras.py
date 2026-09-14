from django import template

register = template.Library()


@register.filter
def initials(name):
    parts = name.split()

    if len(parts) >= 2:
        return parts[0][0].upper() + parts[1][0].upper()

    return parts[0][0].upper()