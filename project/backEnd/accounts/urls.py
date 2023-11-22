from django.urls import path, include
from .views import LoginAPIView, JoinView
from accounts import views


urlpatterns = [
    path('login', LoginAPIView.as_view()),
    path('mypage', view=views.mypage),
    path('join', JoinView.as_view()),
]