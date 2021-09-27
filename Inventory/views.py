from django.shortcuts import render
from .models import User, Product
from .serializers import UserSerializer,ProductSerializer
from rest_framework import generics

class UserListCreate(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class ProductSerializer(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer