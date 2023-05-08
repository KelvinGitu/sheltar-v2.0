from django.shortcuts import render

def index(request):
    return render(request, 'core/index.html')

def about(request):
    return render(request, 'core/about.html')

def properties(request):
    return render(request, 'core/properties.html')

def sheltarGO(request):
    return render(request, 'core/sheltarGO.html')

def contact(request):
    return render(request, 'core/contact.html')