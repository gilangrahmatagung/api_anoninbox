from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import UserVerification


User = get_user_model()
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True) # agar tidak ditampilkan pas Response

    class Meta:
        model = User
        fields = '__all__'

class AskUserVerificationSerializer(serializers.Serializer):
    email = serializers.EmailField()

class CheckUserVerificationSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(write_only=True)
    verification_token = serializers.CharField(write_only=True)

    class Meta:
        model = UserVerification
        fields = '__all__'

class CheckPasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()
    verification_token = serializers.CharField()
    password = serializers.CharField()
    