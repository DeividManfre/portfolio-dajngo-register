from rest_framework import serializers
from .models import User, Product

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'password')

class ProductSerializer(serializers.ModelSerializer):
        class Meta:
            model = Product
            fields = ('id', 'name', 'code', 'size')

