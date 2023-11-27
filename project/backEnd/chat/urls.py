from django.urls import path
from .views import *

urlpatterns = [
    path("", RolePlayingRoomAPIView.as_view(), name = "get_chat_list"), 
    path('create/', CreateRolePlayingRoomAPIView.as_view()),
    path('<int:pk>/delete/', DeleteRolePlayingRoomAPIView.as_view()),
    # path('<int:pk>/edit/', RolePlayingRoomAPIView.as_view()),
]