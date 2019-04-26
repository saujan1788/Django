import socket

from django import template

# To be a valid tag library, the module must contain a module-level
# variable named register that is a template.Library instance, in
# which all the tags and filters are registered

register = template.Library()


#@register.simple_tag
def get_general_info():
    """ Prints the info of the given host"""
    host_name = socket.gethostname()
    # gets the ip address by taking hostname as an argument
    ip_address = socket.gethostbyname('localhost')
    return {
        'host_name': host_name,
        'ip_address': ip_address
    }

register.simple_tag(get_general_info)
# Nevertheless, you may find yourself needing functionality that is not
#  covered by the core set of template primitives. You can extend the
#  template engine by defining custom tags and filters using Python,
#  and then make them available to your templates using the {% load %}
#   tag.
