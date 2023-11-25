from django.urls import path
from .views import RolePlayingRoomAPIView

urlpatterns = [
    path('create/', RolePlayingRoomAPIView.as_view()),
]