from django.shortcuts import render

def index(request):
    template_name = 'catalog/index.html'
    return render(request, template_name)