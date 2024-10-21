from django.shortcuts import render, redirect
from .models import Documentos

# Create your views here.
def home(request):
    documentosListados = Documentos.objects.all()
    return render(request, "gestionRecibidos.html", {"documentos":documentosListados})

def registroRecibido(request):
    codigo = request.POST['txtCodigo']
    fecha = request.POST['fecha']
    hora = request.POST['hora']
    referencia = request.POST['referencia']
    institucion = request.POST['institucion']
    remitente = request.POST['remitente']
    cargoRemitente = request.POST['cargoRemitente']
    observacion = request.POST['observacion']
    fojas = request.POST['fojas']
    estado = request.POST['estado']
    
    documentos = Documentos.objects.create(
        codigo=codigo, fecha=fecha, hora=hora,referencia=referencia,
        institucion=institucion,remitente=remitente,cargoRemitente=cargoRemitente,
        observacion=observacion,fojas=fojas,estado=estado
    )
    return redirect('/')

def edicionRecibido (request, codigo): 
        documentos = Documentos.objects.get(codigo=codigo)
                                                        #Aqui se define como se llamara la variable en la plantilla
        return render(request, 'edicionRecibido.html', {"documentos":documentos})

def editarRecibido(request):
     codigo = request.POST['txtCodigo']
     fecha = request.POST['fecha']
     hora = request.POST['hora']
     referencia = request.POST['referencia']
     institucion = request.POST['institucion']
     remitente = request.POST['remitente']
     cargoRemitente = request.POST['cargoRemitente']
     observacion = request.POST['observacion']
     fojas = request.POST['fojas']
     estado = request.POST['estado']

     #Listamos los datos de Documentos
     documentos = Documentos.objects.get(codigo=codigo)
     documentos.codigo = codigo
     documentos.fecha = fecha   
     documentos.hora = hora
     documentos.referencia = referencia
     documentos.institucion = institucion
     documentos.remitente = remitente
     documentos.cargoRemitente = cargoRemitente
     documentos.observacion = observacion
     documentos.fojas = fojas
     documentos.estado = estado
     
     documentos.save()
     return redirect('/')
     
