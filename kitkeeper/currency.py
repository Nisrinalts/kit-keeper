from django import template
register = template.Library()

@register.filter
def rupiah(value):
    try:
        value = int(value)
    except (ValueError, TypeError):
        return value
    return f"Rp {value:,}".replace(",", ".")
