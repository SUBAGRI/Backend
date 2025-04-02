from django.contrib import admin
from .models import Order, FacturaRec, Cliente

# Register your models here.
admin.site.register(Order)
admin.site.register(FacturaRec)
admin.site.register(Cliente)