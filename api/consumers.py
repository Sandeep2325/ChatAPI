# chat_backend/consumers.py
from channels.generic.websocket import AsyncWebsocketConsumer
import json
from . models import *
from channels.db import database_sync_to_async

class PersonalChatConsumer(AsyncWebsocketConsumer):
   
    async def connect(self):
        # print("Testing connection And redis")
        request_user=self.scope["user"]
        # print(request_user)
        if request_user.is_authenticated:
            chat_with_user=self.scope['url_route']['kwargs']['id']
            user_ids=[int(request_user.id), int(chat_with_user)]
            user_ids=sorted(user_ids)
            print(user_ids)
            self.room_group_name = f"chat_{user_ids[0]}_{user_ids[1]}"

            print("Connect-----",self.room_group_name)
            print("Connect-----",self.channel_name)

            await self.channel_layer.group_add(
                self.room_group_name,
                self.channel_name
            )
        await self.accept()
    # async def receive(self, text_data=None, bytes_data=None):
    #    data=json.loads(text_data)
    #    message=data["newMessage"]["message"]
    #    recipient_id = data["newMessage"]["recipient_id"]
    #    sender_id =self.scope["user"].id
    #    user_ids = [int(sender_id), int(recipient_id)]
    #    user_ids.sort()
    #    self.room_group_name = f"chat_{user_ids[0]}_{user_ids[1]}"
    #    await self.channel_layer.group_send(
    #        self.room_group_name,
    #        {
    #            "type":"chat_message",
    #            "message":message
    #        }
    #    )
    async def receive(self, text_data=None, bytes_data=None):
        data = json.loads(text_data)
        message = data["newMessage"]["message"]
        recipient_id = data["newMessage"]["recipient_id"]
        sender_id=data["newMessage"]["sender_id"]
        # request_user=self.scope["user"]
        key_id=data["newMessage"]["id"]
        # sender=False
        print(data)
        try:
            recipient_id = int(recipient_id)
            sender_id = self.scope["user"].id
            user_ids = [sender_id, recipient_id]
            user_ids.sort()
            self.room_group_name = f"chat_{user_ids[0]}_{user_ids[1]}"
            # print("Connect-----",self.channel_name)
            await self.channel_layer.group_send(
                self.room_group_name,
                {
                    "type": "chat_message",
                    "message": message,
                    "id":key_id,
                    "sender_id":sender_id
                    # "sender":sender,

                }
            )
            data={
                "thread":self.room_group_name,
                "sender_id":sender_id,
                "reciver_id":recipient_id,
                "message":message
            }
            self.save_messages(data)
        except User.DoesNotExist:
            print(f"User with email '{recipient_id}' does not exist.")

    async def disconnect(self, code):
       print("Disconnected")
       self.channel_layer.group_discard(
           self.room_group_name,
           self.channel_name
       )
    async def chat_message(self, event):
        message=event["message"]
        id=event["id"]
        sender_id=event["sender_id"]
        # sender=event["sender"]
        print("eventttt------",event)
        # recipient_id=event["recipient_id"]
        try:
            # user=User.objects.get(id=str(recipient_id))
            await self.send(text_data=json.dumps({
            "message":message,
            "id":id,
            "sender_id":sender_id
            # "sender":sender
        }))
        except Exception as e:
            print(e)
    @database_sync_to_async   
    def save_messages(self,data):
        print("---------------")
        try:
            sender=User.objects.get(id=int(data["sender_id"]))
            reciever=User.objects.get(id=int(data["recipient_id"]))
            message=data["message"]
            thread=data["thread"]
            Message.objects.create(sender=sender, reciever=reciever, thread_name=thread, message=message).save()
            print("------saved------")
        except Exception as e:
            print(e)