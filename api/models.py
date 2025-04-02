from django.db import models
from django.utils.timezone import now

# Order class que es facturas
class Order(models.Model):
    idOrder = models.AutoField(primary_key=True)
    createdAt = models.DateTimeField(blank=True)  # Valor predeterminado agregado
    fecha = models.DateField(default=now, blank=True)
    numfac=models.TextField(max_length=500, default="", blank=True)
    cliente=models.TextField(max_length=500, default="", blank=True)
    baseimp=models.FloatField(default=0.0, blank=True) 
    IVA=models.FloatField(default=0.0, blank=True)
    IVAimp=models.FloatField(default=0.0, blank=True)
    IRPf=models.FloatField(default=0.0, blank=True)
    IRPfimp=models.FloatField(default=0.0, blank=True)
    total = models.FloatField(default=0.0, blank=True)

    def __str__(self):
        return str(self.cliente + " " + self.numfac)

class FacturaRec(models.Model):
    idOrder = models.AutoField(primary_key=True)
    createdAt = models.DateTimeField(blank=True)  # Valor predeterminado agregado
    fecha = models.DateField(blank=True)
    numfac=models.TextField(max_length=500, default="", blank=True)
    proveedor=models.TextField(max_length=500, default="", blank=True)
    baseimp=models.FloatField(default=0.0, blank=True) 
    IVA=models.FloatField(default=0.0, blank=True)
    IVAimp=models.FloatField(default=0.0, blank=True)
    IRPf=models.FloatField(default=0.0, blank=True)
    IRPfimp=models.FloatField(default=0.0, blank=True)
    total = models.FloatField(default=0.0, blank=True)

    def __str__(self):
        return str(self.proveedor + " " + self.numfac)
    
class Cliente(models.Model):
    idCliente = models.AutoField(primary_key=True)
    nombre = models.TextField(max_length=500, default="", blank=True)
    cif = models.TextField(max_length=500, default="", blank=True)
    direccion = models.TextField(max_length=500, default="", blank=True)
    cp = models.IntegerField(default=40000, blank=True)
    tel = models.IntegerField(default=600600600, blank=True)

    def __str__(self):
        return str(self.nombre + " " + self.cif)
