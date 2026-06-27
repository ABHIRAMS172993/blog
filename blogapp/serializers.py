from rest_framework import serializers
from .models import BlogModel
from django.contrib.auth.models import User


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogModel
        fields = '__all__'


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','email','password']
        extra_kwargs = {
            'password':{'write_only':True}
        }

        def create(self,validated_data):
            return User.objects.create_user(**validated_data)
        

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    