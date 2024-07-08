import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from auctions_product.models import Auctions_user_product
from usermodel.models import CustomUser
from products.models import ProductOrService
from django.utils import timezone


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.room_group_name = f"chat_{self.room_name}"

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )

    # Receive message from WebSocket
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        price = text_data_json["addprice"]
        user = text_data_json["user"]
        slug = text_data_json["slug"]
        user = CustomUser.objects.get(name=user)
        product = ProductOrService.objects.get(slug=slug)
        auctions = Auctions_user_product.objects.get(user=user, product=product)
        auctions.price = auctions.price + abs(int(price))
        auctions.datetime = timezone.now()
        auctions.save()
        win_now = Auctions_user_product.objects.filter(product=product).order_by('-price')[0]
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {"type": "chat.message", "firstnamewin": win_now.user.name, "your_price": auctions.price}
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event

        # Send message to WebSocket
        self.send(text_data=json.dumps({"message": message}))
