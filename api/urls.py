from django.contrib import admin
from django.urls import path, include
from .views import *
from rest_framework import routers
router = routers.DefaultRouter()
# router.register(r'users', UserViewSet, basename="userss")
urlpatterns = [
      path("",home, name="home" ),
      path("users/",UserViewSet.as_view()),
      path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
urlpatterns += router.urls