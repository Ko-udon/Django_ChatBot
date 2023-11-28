# chat/models.py

from django.conf import settings
from django.core.validators import MinLengthValidator
from django.db import models

from typing import TypedDict, Literal, List

class GptMessage(TypedDict):
    role: Literal["system", "user", "assistant"]
    content: str

class RolePlayingRoom(models.Model):
    user_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, default= 1)

    language = models.CharField(
        max_length=10, 
        verbose_name="대화 언어")
    
    situation = models.CharField(
        max_length=100,
        verbose_name="상황")
    
    my_role = models.CharField(max_length=100, verbose_name="내 역할")

    gpt_role = models.CharField(max_length=100, verbose_name="GPT 역할")

    chat_history = models.TextField(verbose_name="채팅 기록", blank=True)

    def get_initial_messages(self) -> List[GptMessage]:
        gpt_name = "역할놀이채팅봇"

        language = self.language
        situation = self.situation
        my_role = self.my_role
        gpt_role = self.gpt_role
        
        system_message = (
            f"너의 이름은 {gpt_name}야. "
            f"유저와 대화를 이어나가면 되."
        )
        
        user_message = (
            f"대화 언어는 {language}로 대화할거야. "
            f"{language}로만 대화하면 되."
            f"{situation} 상황을 가정하고 각자 역할을 부여해서 대화할거야."
            f"내 역할은 {my_role} 이야."
            f"너의 역할은 {gpt_role} 이야."
            f"이제 대화를 시작하자."
        )
        
        return [
            # GptMessage(role="system", content=system_message),
            # GptMessage(role="user", content=user_message),
            system_message, user_message
        ]

