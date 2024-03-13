from django.contrib import admin
from django.urls import path, include
from .views import *
from rest_framework import routers
router = routers.DefaultRouter()
# router.register(r'users', UserViewSet, basename="userss")
urlpatterns = [
      path("",home, name="home" ),
      path("users/",UserViewSet.as_view()),
      path("register/",Register.as_view()),
      path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
      path('messages/', MessageListCreate.as_view(), name='message-list-create'),
      path('getdata/', get_token_data, name='get data'),

]
urlpatterns += router.urls