from rest_framework import serializers
from .models import CustomUser

from django.contrib.auth import authenticate
from django.utils import timezone

# 회원가입
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'email',
            'password'
            ]
        
    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            email = validated_data['email'],
            password = validated_data['password']
        )
        return user
    
# 로그인
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=128, write_only=True)
    last_login = serializers.CharField(max_length=255, read_only=True)
    
    def validate(self, data):
        email = data.get('email', None)
        password = data.get('password', None)
        
        if email is None:
            raise serializers.ValidationError(
                'An email address is required to log in.'
            )
        
        if password is None:
            raise serializers.ValidationError(
                'A password is required to log in.'
            )
        
        user = authenticate(username=email, password=password)
        
        if user is None:
            raise serializers.ValidationError(
                'A user with this email and password was not found'
            )
        
        if not user.is_active:
            raise serializers.ValidationError(
                'This user has been deactivated.'
            )
        
        user.last_login = timezone.now()
        user.save(update_fields=['last_login'])
        
        return {
            'email': user.email,
            'last_login': user.last_login
        }
