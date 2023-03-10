from django.contrib.sessions.models import Session
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.generics import GenericAPIView
from apps.users.models import User
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from apps.users.api.serializers import CustomTokenOntainPairSerializer , CustomUserSerializer

class Login(TokenObtainPairView):
    serializer_class = CustomTokenOntainPairSerializer
    
    def post(self,request,*args,**kwargs):
        username= request.data.get('username','')
        password = request.data.get('password','')
        user = authenticate(
            username=username,
            password=password
        )
        if user:
            login_serializer = self.serializer_class(data = request.data)
            if login_serializer.is_valid():
                user_serializer = CustomUserSerializer(user)
                return Response({
                    'token':login_serializer.validated_data.get('access'),
                    'refresh':  login_serializer.validated_data.get('refresh'),
                    'user':user_serializer.data,
                    'message':'Inicio de session existoso'               
                },status=status.HTTP_200_OK)
            return Response({'error':'Contraseña o nombre Incorrectos'},status=status.HTTP_400_BAD_REQUEST)
        return Response({'error':'Contraseña o nombre Incorrectos'},status=status.HTTP_400_BAD_REQUEST)
    

class Logout(GenericAPIView):
    def post(self,request,*args,**kwargs):
        user = User.objects.filter(id=request.data.get('user',0))
        if user.exists():
            RefreshToken.for_user(user.first())
            return Response({'message':'Session cerrada correctamente'},status=status.HTTP_200_OK)
        return Response({'error':'No existe usuario con eso datos'},status=status.HTTP_400_BAD_REQUEST)