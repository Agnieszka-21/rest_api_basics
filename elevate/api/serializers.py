from rest_framework import serializers
from django.contrib.auth.models import User

from . models import Product


class ProductSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price']


class RegistrationSerializer(serializers.ModelSerializer):

    password2 = serializers.CharField(style={'input_type': 'password'}, write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def save(self):
        user = User(
            username=self.validated_data['username'],
            email=self.validated_data['email'],
        )
        password=self.validated_data['password']
        password2=self.validated_data['password2']

        if password != password2:
            raise serializers.ValidationError({'password': 'Your passwords do not match'})
        
        user.set_password(password)
        user.save()
        return user

    