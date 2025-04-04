from django.contrib import admin
from .models import Order, FacturaRec, Cliente, CodigoProducto

# Register your models here.
admin.site.register(Order)
admin.site.register(FacturaRec)
admin.site.register(Cliente)
admin.site.register(CodigoProducto)