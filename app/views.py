from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View, TemplateView
# Create your views here.

## Function Based View
def fbv_string(request):
    return HttpResponse("<center><h1>This is function based view</h1></center>")


## Class Based View
class cbv_string(View):
    def get(self, request):
        return HttpResponse("<center><h1>This is class based view</h1></center>")


## Rendering HTML Page by using class based view
class cbv_html(TemplateView):
    template_name = "index.html"