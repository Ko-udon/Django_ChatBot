# chat/models.py

from django.conf import settings
from django.core.validators import MinLengthValidator
from django.db import models


class RolePlayingRoom(models.Model):
    # class Language(models.TextChoices):
    #     KOREAN = "ko-KR", "Korean"
    #     ENGLISH = "en-US", "English"
    #     JAPANESE = "ja-JP", "Japanese"

    # class Meta:
    #     ordering = ["-pk"]

    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default= 1)

    language = models.CharField(
        max_length=10, 
        verbose_name="대화 언어")
    
    situation = models.CharField(
        max_length=100,
        verbose_name="상황")
    
    my_role = models.CharField(max_length=100, verbose_name="내 역할")

    gpt_role = models.CharField(max_length=100, verbose_name="GPT 역할")