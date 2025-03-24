from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Book
class RegisterSerializer(serializers.ModelSerializer):
    password2=serializers.CharField(write_only=True)
    class Meta:
        model=User
        fields=['username','email','password','password2']
        
    def validate_email(self, value):
        """Check if the email is already taken."""
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email is already in use.")
        return value
    def validate(self, data):
        if data['password'] != data["password2"]:
            raise serializers.ValidationError("password must match")
        return data
    
    def create(self, validated_data):
        user=User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
        )
        return user
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'
        
 


    