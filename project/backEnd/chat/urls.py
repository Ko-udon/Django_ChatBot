from django.urls import path
from .views import *

urlpatterns = [
    path("", RolePlayingRoomAPIView.as_view()), 
    path('create/', CreateRolePlayingRoomAPIView.as_view()),
    # path('<int:pk>/edit/', RolePlayingRoomAPIView.as_view()),
]