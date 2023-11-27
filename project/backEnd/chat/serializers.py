from rest_framework import serializers
from .models import RolePlayingRoom

from django.contrib.auth import authenticate
from django.utils import timezone
from django.conf import settings
# User serializer
class CreateChatSerializer(serializers.ModelSerializer):
    
    class Meta:
        ordering = ["-pk"]
        model = RolePlayingRoom
        fields = [
            "pk",
            "language",
            "situation",
            "my_role",
            "gpt_role",
        ]

    def create(self, validated_data):
        user = self.context['user']
        chat = RolePlayingRoom.objects.create(
            user_id=user
            ,**validated_data
        )
        return chat
    
    def update(self, chat, validated_data):
        chat.language = validated_data.get('language', chat.language)
        chat.situation = validated_data.get('situation', chat.situation)
        chat.my_role = validated_data.get('my_role', chat.my_role)
        chat.gpt_role = validated_data.get('gpt_role', chat.gpt_role)
        chat.save()
        return chat
