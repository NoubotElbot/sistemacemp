from django.shortcuts import render
from django.views.generic import View,TemplateView

# Create your views here.

class Home(TemplateView):
    template_name ='index.html'

# def home(request):
#     return render(request, 'index.html')