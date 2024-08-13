from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.views.generic.base import TemplateView
from django.shortcuts import render

# def home(request):
#     return render(request, "core/home.html")

# def sample(request):
#     return render(request, "core/sample.html")

class HomePageView(TemplateView):
    template_name = "core/home.html"
    
    # def get_context_data(self, **kwargs):
        
    #     context = super().get_context_data(**kwargs)
    #     context['title'] = "Mi SuperWeb PlayGroup"
    #     return context
    
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name,{'title': "Mi SuperWeb PlayGroup"})
        
    
    
    

class SampleView(TemplateView):
    template_name = "core/sample.html"
    
    