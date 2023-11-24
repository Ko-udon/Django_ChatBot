# chat/forms.py

from django import forms
from .models import RolePlayingRoom



class RolePlayingRoomForm(forms.ModelForm):
    class Meta:
        model = RolePlayingRoom
        fields = [
            "language",
            "situation",
            "my_role",
            "gpt_role",
        ]