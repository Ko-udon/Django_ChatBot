# authentication > api > views.py
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from .serializers import LoginSerializer, JoinSerializer


# rendering
from .renderers import UserJSONRenderer

# test

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer



class LoginAPIView(APIView):
    # permission_classes = (AllowAny,)
    # renderer_classes = (UserJSONRenderer,)
    # serializer_class = LoginSerializer
    
    # # 1.
    # def post(self, request):
    #     # 2.
    #     user = request.data
        
    #     # 3.
    #     serializer = self.serializer_class(data=user)
    #     serializer.is_valid(raise_exception=True)
        
    #     # 4.
    #     return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        user = request.data

        serializer = LoginSerializer(data = user)
        serializer.is_valid(raise_exception=True)

        token = TokenObtainPairSerializer.get_token(user)
        refresh_token = str(token)
        access_token = str(token.access_token)
        res = Response(
            {
                "user": user.email,
                "message": "login successs",
                "token": {
                    "access": access_token,
                    "refresh": refresh_token,
                },
            },
            status=status.HTTP_200_OK,
        )
        
        # jwt 토큰 => 쿠키에 저장
        res.set_cookie("access", access_token, httponly=True)
        res.set_cookie("refresh", refresh_token, httponly=True)
        
        return res
    

      # return Response(serializer.data, status=status.HTTP_200_OK)
    


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def mypage(request):
    content = {'message': '반갑습니다,' + str(request.user.email) + '님!'}
    
    return Response(content)

class JoinView(APIView):
    def post(self, request):
        serializer = JoinSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            
            # jwt 토큰 접근
            token = TokenObtainPairSerializer.get_token(user)
            refresh_token = str(token)
            access_token = str(token.access_token)
            res = Response(
                {
                    "user": serializer.data,
                    "message": "register successs",
                    "token": {
                        "access": access_token,
                        "refresh": refresh_token,
                    },
                },
                status=status.HTTP_200_OK,
            )
            
            # jwt 토큰 => 쿠키에 저장
            res.set_cookie("access", access_token, httponly=True)
            res.set_cookie("refresh", refresh_token, httponly=True)
            
            return res
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    