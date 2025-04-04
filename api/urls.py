from django.urls import path
from . import views

from django.urls import path
from . import views

urlpatterns = [
    # Order
    path('orders/', views.OrderListCreate.as_view(), name='order-list'),
    path('orders/<int:pk>/', views.OrderDetail.as_view(), name='order-detail'),
    path('facturasRec/', views.FacturaRecListCreate.as_view(), name='facturasRec-list'),
    path('facturasRec/<int:pk>/', views.FacturaRecDetail.as_view(), name='facturasRec-detail'),
    path('clientes/', views.ClienteListCreate.as_view(), name='cliente-list'),
    path('clientes/<int:pk>/', views.ClienteDetail.as_view(), name='cliente-detail'),
    path('codigoProducto/', views.CodigoProductoCreate.as_view(), name='codigoProducto-list'),
    path('codigoProducto/<int:pk>/', views.CodigoProductoDetail.as_view(), name='codigoProducto-detail'),

]
