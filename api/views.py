from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Order, FacturaRec, Cliente
from .serializers import OrderSerializer, UserSerializer, FacturaRecSerializer, ClienteSerializer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

# User Views
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

@csrf_exempt
def delete_user(request, pk):
    if request.method == 'DELETE':
        try:
            user = User.objects.get(id=pk)
            user.delete()
            return JsonResponse({'message': 'User deleted successfully'}, status=200)
        except User.DoesNotExist:
            return JsonResponse({'message': 'User not found'}, status=404)
    return JsonResponse({'message': 'Invalid request'}, status=400)


# Order Views
class OrderListCreate(generics.ListCreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Order.objects.all()

    def perform_create(self, serializer):
        serializer.save()

class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [AllowAny]

#FacturaRec Views
class FacturaRecListCreate(generics.ListCreateAPIView):
    serializer_class = FacturaRecSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return FacturaRec.objects.all()

    def perform_create(self, serializer):
        serializer.save()

class FacturaRecDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FacturaRec.objects.all()
    serializer_class = FacturaRecSerializer
    permission_classes = [AllowAny]

#Cliente Views
class ClienteListCreate(generics.ListCreateAPIView):
    serializer_class = ClienteSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Cliente.objects.all()

    def perform_create(self, serializer):
        serializer.save()

class ClienteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    permission_classes = [AllowAny]