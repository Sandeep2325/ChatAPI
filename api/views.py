from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework import permissions, viewsets
from .serializers import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .tokenverify import verify_and_extract_token_data
import json
# Create your views here.
@csrf_exempt
def home(request):
    if request.method=="GET":
        return JsonResponse({"message":True}) 
    name=request.POST
    print(name)
    return JsonResponse({"Post":name})

class UserViewSet(APIView):
    permission_classes=(IsAuthenticated,)
    authentication_classes=[JWTAuthentication,]
    def get(self, request, format=None):
        
        """
        Return a list of all users.
        """
        try:
            user_obj=User.objects.exclude(id=request.user.id)
            serializer=UserSerializer(user_obj,many=True)
            return Response(serializer.data, status=200)
        except Exception as e:
            print("error in getting userlist", (e))
            return Response({"error":"Error getting user list"}, status=400)
    

class Register(APIView):
    def post(self, request):
        print(request.data)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Account created successfully", "data": serializer.data}, status=status.HTTP_201_CREATED)
        return Response({"error":"Something went wrong","data":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class MessageListCreate(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

async def get_token_data(request):
    if request.method=="POST":
        token=request.POST.get["token"]
        res=verify_and_extract_token_data(token)
        return res
    else:
        print(request.GET["token"])
        token=request.GET["token"]
        res=await verify_and_extract_token_data(token)
        id={"id":res.id}
        return JsonResponse(id, safe=False)
