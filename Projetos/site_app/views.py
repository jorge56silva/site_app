from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "site_app/index.html")

def sobre(request):
    return render(request, "site_app/sobre.html")

def contato(request):
    return render(request, "site_app/contato.html")