# chat 방 관련
from django.contrib.admin.views.decorators import staff_member_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy

from .models import RolePlayingRoom

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CreateChatSerializer

from rest_framework_simplejwt.authentication import JWTAuthentication

from chatProject.settings import SECRET_KEY
from accounts.models import CustomUser as User
import jwt
from django.shortcuts import render, get_object_or_404

# chatbot 관련
import os
import openai

from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
from django.http import JsonResponse

# 하루 요청 횟수 제한
# from rest_framework.throttling import UserRateThrottle

#########################################################################


# 목록조회
class RolePlayingRoomAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    model = RolePlayingRoom

    def get(self, request):
        access = request.COOKIES['access']
        payload = jwt.decode(access, SECRET_KEY, algorithms=['HS256'])
        pk = payload.get('user_id')
        user = get_object_or_404(User, pk=pk)

        chats = RolePlayingRoom.objects.filter(user_id_id = user.pk)
        serializer = CreateChatSerializer(chats, many = True)

        return Response(
                {
                    "chat_list": serializer.data,
                },
                status=status.HTTP_200_OK,
            ) 


# 생성
class CreateRolePlayingRoomAPIView(APIView):
    authentication_classes = [JWTAuthentication]

    def post(self, request):
        access = request.COOKIES['access']
        payload = jwt.decode(access, SECRET_KEY, algorithms=['HS256'])
        pk = payload.get('user_id')
        user = get_object_or_404(User, pk=pk)     

        serializer = CreateChatSerializer(data=request.data, context={'user': user})
        if serializer.is_valid():
            chat = serializer.save()
            print('success')
            return Response(
                {
                    "success": True,
                },
                status=status.HTTP_200_OK,
            )
        # 예외처리 필요
        else:
            print("fail")
            return Response(
                {
                    "success": False
                },
                status=status.HTTP_200_OK,
            )


# 상세보기
class DetailRolePlayingRoomAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    
    def get(self, request, pk): 
        chat = RolePlayingRoom.objects.get(pk=pk)
        serializer = CreateChatSerializer(chat)
        return Response(
                {
                    "chat_list": serializer.data,
                },
                status=status.HTTP_200_OK,
            ) 

# 수정
class UpdateRolePlayingRoomAPIView(APIView):
    authentication_classes = [JWTAuthentication]

    def post(self, request, pk):
        chat = RolePlayingRoom.objects.get(pk=pk)
        
        serializer = CreateChatSerializer(chat, data=request.data)
        if serializer.is_valid():
            chat = serializer.save()
            print('success')
            return Response(
                {
                    "success": True,
                },
                status=status.HTTP_200_OK,
            )

# 삭제
class DeleteRolePlayingRoomAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    model = RolePlayingRoom

    def delete(self, request, pk):
        chat = RolePlayingRoom.objects.get(pk=pk)
        chat.delete()

        return Response(
                {
                    "Delete_result": "Success"
                },
                status=status.HTTP_200_OK,
            ) 
    

# chatGPT
class chatGPT(APIView):
    model = RolePlayingRoom

    def ask_chatbot(message, pk):
        chat = RolePlayingRoom.objects.get(pk=pk)
        chatSetting = chat.get_initial_messages()

        response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", 
                    "content": chatSetting[0]},
                    {"role": "user", "content": chatSetting[1]},
                    {"role": "user", "content": message},
                ]
        )

        answer = response.choices[0].message.content.strip()
        return answer
    
    def post(self, request, pk):
        chat = RolePlayingRoom.objects.get(pk=pk)

        message = request.data.get('message')
        chat.chat_history+='<tap>'+'user: '+message+' '

        answer = chatGPT.ask_chatbot(message, pk)
        
        chat.chat_history+='<tap>'+'system: '+answer+' '
        chat.save()
        return Response(
            {
                "answer": answer
            },
            status=status.HTTP_200_OK,
        ) 



