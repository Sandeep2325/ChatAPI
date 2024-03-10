from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import make_password
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'email','password',"first_name", "last_name"]
    def create(self, validated_data):
        validated_data['password'] = make_password(validated_data.get('password'))
        return super().create(validated_data)
