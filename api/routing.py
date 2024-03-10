# chat_backend/routing.py
from django.urls import re_path
from .consumers import *
from django.urls import path
websocket_urlpatterns = [
   path("ws/chat/<int:id>/", PersonalChatConsumer.as_asgi())
]
