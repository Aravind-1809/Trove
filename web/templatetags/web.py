from datetime import date

from django.conf import settings
from django import template

register = template.Library()


@register.filter
def is_production(value):
    try:
        environment = settings.ENVIRONMENT.upper()
    except (KeyError, AttributeError):
        environment = None

    return environment == 'PROD'
