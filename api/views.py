from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions, viewsets
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
@csrf_exempt
def home(request):
    if request.method=="GET":
        return JsonResponse({"message":True}) 
    name=request.POST
    print(name)
    return JsonResponse({"Post":name})

class UserViewSet(APIView):
    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)
    def post(self, request):
        print(request.data)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"Account created successfully"},serializer.data, status=status.HTTP_201_CREATED)
        return Response({"error":"Something went wrong"},serializer.errors, status=status.HTTP_400_BAD_REQUEST)