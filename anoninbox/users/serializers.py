import secrets
from django.core.mail import send_mail
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import UserVerification


User = get_user_model()
class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True) # agar tidak ditampilkan pas Response

    class Meta:
        model = User
        fields = '__all__'
    
    def create(self, validated_data):
        return User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            is_active=False
        )

class AskUserVerificationSerializer(serializers.ModelSerializer):
    verification_token = serializers.ReadOnlyField()

    class Meta:
        model = UserVerification
        fields = '__all__'

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
    