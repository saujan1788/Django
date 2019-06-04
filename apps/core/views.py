import re
import socket
import uuid
from django.views import generic

from apps.core.forms import SubnetForm, ConvertForm, ExpandForm, ValidIPv6Form


class HomePageView(generic.TemplateView):
    template_name = "home.html"


class SubnetView(generic.FormView):
    form_class = SubnetForm
    success_url = "/subnet"
    template_name = "subnet.html"

    def form_valid(self, form):
        result = form.calculate_subnet()
        return self.render_to_response(self.get_context_data(result=result))


class ConvertView(generic.FormView):
    form_class = ConvertForm
    success_url = "/convert"
    template_name = "convert.html"

    def form_valid(self, form):
        result = form.convert_dec_to_bin()
        return self.render_to_response(self.get_context_data(result=result))


class ValidIPv6View(generic.FormView):
    form_class = ValidIPv6Form
    success_url = "/valid"
    template_name = "valid.html"

    def form_valid(self, form):
        result = form.valid_ipv6()
        return self.render_to_response(self.get_context_data(result=result))


class ExpandView(generic.FormView):
    form_class = ExpandForm
    success_url = "/expand"
    template_name = "expand.html"

    def form_valid(self, form):
        result = form.expand_ipv6()
        return self.render_to_response(self.get_context_data(result=result))


class GeneralInfoView(generic.TemplateView):
    template_name = "general_info.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        host_name = socket.gethostname()
        # gets the ip address by taking hostname as an argument
        ip_address = socket.gethostbyname('localhost')
        context['host_name'] = host_name
        context['ip_address'] = ip_address
        return context


class MacAddressView(generic.TemplateView):
    template_name = "mac_address.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        mac_address = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
        context['mac_address'] = mac_address
        return context
