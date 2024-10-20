from django.shortcuts import render
from .models import Documentos

# Create your views here.
def home(request):
    documentosListados = Documentos.objects.all()
    return render(request, "gestionRecibidos.html", {"documentos":documentosListados})


