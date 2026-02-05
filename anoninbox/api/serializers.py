from rest_framework import serializers
from cryptography.fernet import Fernet
from django.conf import settings

from .models import *



fernet = Fernet(settings.MESSAGE_ENCRYPTION_KEY)

class BoxSerializer(serializers.ModelSerializer):
    box_maker = serializers.ReadOnlyField(source="box_maker_id")
    
    class Meta:
        model = Box
        fields = '__all__'

class ThreadSerializer(serializers.ModelSerializer):
    user_email = serializers.ReadOnlyField(source="user_email_id")

    class Meta:
        model = Thread
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    thread = serializers.PrimaryKeyRelatedField(read_only=True)
    is_author_box_maker = serializers.ReadOnlyField()

    class Meta:
        model = Message
        fields = '__all__'

    def to_internal_value(self, data):
        data = super().to_internal_value(data)

        if data["message_title"] is not None:
            print("MASUK SINI1")
            data["message_title"] = fernet.encrypt(data["message_title"].encode()).decode()
        data["message_body"] = fernet.encrypt(data["message_body"].encode()).decode()

        return data
    
    def to_representation(self, instance):
        data = super().to_representation(instance)

        if data["message_title"] is not None:
            print("MASUK SINI2")

            data["message_title"] = fernet.decrypt(data["message_title"].encode()).decode()
        data["message_body"] = fernet.decrypt(data["message_body"].encode()).decode()

        return data

# -------------------------------------------------------------------

class ThreadAndMessagesSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True)

    class Meta:
        model = Thread # bukan Messages ke Thread, karena queryset nya Thread
        fields = '__all__'


class StartThreadSerializer(serializers.Serializer):  # karena nested serializer tidak bisa untuk create jadi gabisa gabung sama thread and messages
    box = serializers.PrimaryKeyRelatedField(read_only=True)
    non_user_email = serializers.EmailField(max_length=50, required=False)
    
    message_title = serializers.CharField(max_length=50, required=False)
    message_body = serializers.CharField(max_length=1000)
    is_author_box_maker = serializers.BooleanField(read_only=True)

    def to_internal_value(self, data):
        data = super().to_internal_value(data)

        if data["message_title"] is not None:
            print("MASUK SINI3")

            data["message_title"] = fernet.encrypt(data["message_title"].encode()).decode()
        
        data["message_body"] = fernet.encrypt(data["message_body"].encode()).decode()

        return data
    
    def to_representation(self, instance):
        data = super().to_representation(instance)

        if data["message_title"] is not None:
            print("MASUK SINI4")

            data["message_title"] = fernet.decrypt(data["message_title"].encode()).decode()
        
        data["message_body"] = fernet.decrypt(data["message_body"].encode()).decode()

        return data