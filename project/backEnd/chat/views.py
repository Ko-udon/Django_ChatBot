from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
# from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import RolePlayingRoomForm
from .models import RolePlayingRoom

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CreateChatSerializer

# 아직 로그인 기능을 구현하지 않았기에, admin 앱의 로그인 기능을 활용토록 합니다.
# 
class RolePlayingRoomAPIView(APIView):
    def post(self, request):
        user = str(request.user.email)
        serializer = CreateChatSerializer(data=request.data, context={'request': request})
        if serializer.is_valid():
            chat = serializer.save()
            
            # # jwt 토큰 접근
            # token = TokenObtainPairSerializer.get_token(user)
            # refresh_token = str(token)
            # access_token = str(token.access_token)
            # res = Response(
            #     {
            #         "user": serializer.data,
            #         "message": "register successs",
            #         "token": {
            #             "access": access_token,
            #             "refresh": refresh_token,
            #         },
            #     },
            #     status=status.HTTP_200_OK,
            # )
            
            return Response(
                {
                    "success": True,
                    "user": user,
                },
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {
                    "success": False
                },
                status=status.HTTP_200_OK,
            )


    # model = RolePlayingRoom
    # form_class = RolePlayingRoomForm
    # success_url = reverse_lazy("role_playing_room_new")  # 페이지 성공 후에 이동할 페이지 주소 지정

    

    # def form_valid(self, form):
    #     role_playing_room = form.save(commit=False)
    #     role_playing_room.user = self.request.user
    #     response = super().form_valid(form)
    #     messages.success(self.request, "새로운 채팅방을 생성했습니다.")
    #     return response

