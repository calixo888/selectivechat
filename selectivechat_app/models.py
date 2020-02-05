from django.db import models

class ChatRoom(models.Model):
    chat_id = models.CharField(max_length=100, primary_key=True)
    chat_room_name = models.CharField(max_length=100)

    def __str__(self):
        return self.chat_room_name
