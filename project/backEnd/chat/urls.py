from django.urls import path
from .views import RolePlayingRoomAPIView

urlpatterns = [
    path('new/', RolePlayingRoomAPIView.as_view()),
]