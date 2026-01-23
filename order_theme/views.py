from django.shortcuts import render

def index(request):
    template_name = 'order_theme/index.html'
    return render(request, template_name)