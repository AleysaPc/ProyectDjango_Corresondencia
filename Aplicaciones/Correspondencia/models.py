from django.db import models

# Create your models here.
class Documentos(models.Model):
    codigo = models.CharField(primary_key=True, max_length=5)
    fecha=models.DateField()
    hora = models.TimeField()
    #citeRemitente= models.CharField(max_length=10)
    referencia=models.CharField(max_length=255)
    institucion=models.CharField(max_length=100)
    #apellidosRemitente=models.CharField(max_length=30)
    remitente=models.CharField(max_length=30)
    cargoRemitente=models.CharField(max_length=30)
    observacion=models.CharField(max_length=255)
    fojas=models.IntegerField()
    estado=models.CharField(max_length=20)

    #Para visualizar un formato mas comprensible
    def __str__(self):
        return f"{self.codigo} - {self.referencia} ({self.nombreRemitente} {self.apellidosRemitente})"

