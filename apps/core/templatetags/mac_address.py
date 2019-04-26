import re
import uuid

from django import template

register = template.Library()


@register.simple_tag
def get_mac_address():
    return ':'.join(re.findall('..', '%012x' % uuid.getnode()))

register.simple_tag(get_mac_address)
