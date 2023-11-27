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