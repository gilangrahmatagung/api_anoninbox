from rest_framework import serializers
from django.db import transaction

from .models import *

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