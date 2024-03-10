from channels.middleware import BaseMiddleware
from rest_framework.exceptions import AuthenticationFailed
from django.db import close_old_connections
from .tokenverify import verify_and_extract_token_data

class JWTWEBsocketMiddleware(BaseMiddleware):
    async def __call__(self, scope, recieve, send):
        close_old_connections()
        query_string=scope.get("query_string", b"").decode("utf-8")
        quesry_parameters=dict(qp.split("=") for qp in query_string.split("&"))
        token=quesry_parameters.get("token", None)
       
        if token is None:
            await send({
                "type":"websocket.close",
                "code":4000
            })
            print("closedd")
            
        try:
            user=await verify_and_extract_token_data(token)
            print(user)
            if user is not None:
                scope["user"]=user
            else:
                await send({
                    "type":"websocket.close",
                    "code":4000
                })
            return await super().__call__(scope, recieve, send)
                
        except AuthenticationFailed:
            await send({
                    "type":"websocket.close",
                    "code":4002
                })
            print("closeddd")