from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import make_password
from .models import Message
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    username=serializers.CharField(read_only=True)
    class Meta:
        model = User
        fields = ["id", "username","email", "password", "first_name", "last_name"]  # Include the username field in fields list
        extra_kwargs = {"id": {"read_only": True},"username":{"read_only"}}

    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        validated_data["username"]=validated_data.get('email') 
        return super().create(validated_data)


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'