from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny

from .serializers import UserSerializer


class RegisterView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

class LoginView(APIView):
    serializer_class = UserSerializer
    
    def post(self, request):
        user = authenticate(
            request,
            email=request.data.get('email'),
            password=request.data.get('password')
        )

        if user:
            login(request, user)
            return Response({"status": "Logged in"})
        
        return Response({"error": "Invalid credentials"}, status=400)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        logout(request)
        return Response({"status": "Logged out"})