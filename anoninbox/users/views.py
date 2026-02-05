from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
import secrets

from .models import *
from .serializers import *


class RegisterView(generics.CreateAPIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer

class AskUserVerificationView(APIView):
    permission_classes = [AllowAny]
    serializer_class = AskUserVerificationSerializer

    def post(self, request):
        serializer = AskUserVerificationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        try:
            if User.objects.get(email=serializer.validated_data['email']): # cek apakah sudah registrasi
                # buat token
                token_to_db = secrets.token_urlsafe(16)
                # kirim ke user
                send_mail(
                    subject="AnonInbox | Verifikasi Akun",
                    message=f"""
                                Silakan lakukan verifikasi dengan {token_to_db}
                            """,
                    recipient_list=[serializer.validated_data['email']],
                    from_email=None,
                    fail_silently=False
                )
                # simpan ke db
                UserVerification.objects.update_or_create(
                    email=serializer.validated_data['email'],
                    defaults={'verification_token':token_to_db}
                )

                return Response({"message":"Token verifikasi telah dikirim"})
            else:
                return Response({"error":"Permintaan verifikasi gagal"}, status=400)
        except Exception as e:
            print(f"ERROR: {e}")
            return Response({"error":"User dengan email tidak ditemukan"}, status=400)

class CheckUserVerificationView(APIView):
    permission_classes = [AllowAny]
    serializer_class = CheckUserVerificationSerializer

    def post(self, request):
        serializer = CheckUserVerificationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            token_in_db = UserVerification.objects.get(email=serializer.validated_data['email']).verification_token

            if token_in_db==serializer.validated_data['verification_token']:
                user = User.objects.get(email=serializer.validated_data['email'])
                user.is_active=True
                user.save()

                UserVerification.objects.get(email=serializer.validated_data['email']).delete()

                return Response({"message":"Berhasil memverifikasi akun"})
            else:
                return Response({"error":"Gagal memverifikasi akun"}, status=400)

        except:
            return Response({"error":"User dengan email tidak ditemukan"}, status=400)

class LoginView(APIView):
    permission_classes = [AllowAny]
    serializer_class = UserSerializer
    
    def post(self, request):
        user = authenticate(
            request,
            email=request.data.get('email'),
            password=request.data.get('password')
        )

        if user:
            login(request, user)

            return Response({"message": "Login succeeded"})
        
        return Response({"error": "Invalid credentials"}, status=401)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = UserSerializer
    
    def get(self, request):
        logout(request)

        return Response({"message": "Logged out"})

class AskPasswordResetView(APIView):
    permission_classes = [AllowAny]
    serializer_class = AskUserVerificationSerializer

    def post(self, request):
        serializer = AskUserVerificationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        try:
            if User.objects.get(email=serializer.validated_data['email']): # cek apakah sudah registrasi
                # buat token
                token_to_db = secrets.token_urlsafe(16)
                # kirim ke user
                send_mail(
                    subject="AnonInbox | Atur Ulang Sandi",
                    message=f"""
                                Silakan lakukan atur ulang sandi dengan {token_to_db}
                            """,
                    recipient_list=[serializer.validated_data['email']],
                    from_email=None,
                    fail_silently=False
                )
                # simpan ke db
                UserVerification.objects.update_or_create(
                    email=serializer.validated_data['email'],
                    defaults={'verification_token':token_to_db}
                )

                return Response({"message":"Token atur ulang sandi telah dikirim"})
            else:
                return Response({"error":"Permintaan atur ulang sandi gagal"}, status=400)
        except Exception as e:
            print(f"ERROR: {e}")
            return Response({"error":"User dengan email tidak ditemukan"}, status=400)

class CheckPasswordResetView(APIView):
    permission_classes = [AllowAny]
    serializer_class = CheckPasswordResetSerializer

    def post(self, request):
        serializer = CheckPasswordResetSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            token_in_db = UserVerification.objects.get(email=serializer.validated_data['email']).verification_token

            if token_in_db==serializer.validated_data['verification_token']:
                User.objects.get(email=serializer.validated_data['email']).delete()

                User.objects.create_user(
                    email=serializer.validated_data['email'],
                    password=serializer.validated_data['password'],
                    is_active=True
                )

                UserVerification.objects.get(email=serializer.validated_data['email']).delete()

                return Response({"message":"Berhasil mengatur ulang sandi"})
            else:
                return Response({"error":"Gagal mengatur ulang sandi"}, status=400)
        
        except:
            return Response({"error":"User dengan email tidak ditemukan"}, status=400)
        