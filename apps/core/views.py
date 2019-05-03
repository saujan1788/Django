
from django.views import generic

from apps.core.forms import SubnetForm


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

