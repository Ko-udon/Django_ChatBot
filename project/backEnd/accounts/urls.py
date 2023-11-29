from django.urls import path, include
from .views import SignUpView, UserAuthAPIView
from accounts import views

# 토큰 재발급
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('signup/', SignUpView.as_view()), # 회원가입
    path("auth/", UserAuthAPIView.as_view()), # post 로그인, delete 로그아웃, get 유저확인
]