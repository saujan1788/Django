
from django.views.generic import TemplateView
from django.shortcuts import render
from django.http import HttpResponse
from .subnet import user_form




class HomePageView(TemplateView):
    template_name = "home.html"
    context_object_name = 'home'

    def user_input(request):
        if request.method == 'POST':
            form = user_form(request.POST)
            if form.is_valid():

                ip = form.cleaned_data['ip']
                mask = form.cleaned_data['mask']

        form = user_form()
        return render(request,'home.html',{'form':form})
