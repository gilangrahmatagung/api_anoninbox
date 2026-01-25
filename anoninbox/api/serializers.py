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

    class Meta:
        model = Message
        fields = '__all__'

# -------------------------------------------------------------------

class ThreadAndMessagesSerializer(serializers.ModelSerializer):
    messages = MessageSerializer(many=True)

    class Meta:
        model = Thread # bukan Messages ke Thread, karena queryset nya Thread
        fields = '__all__'


class StartThreadSerializer(serializers.Serializer):
    box = serializers.IntegerField(write_only=True)

    message_title = serializers.CharField(max_length=50, required=False)
    message_body = serializers.CharField(max_length=1000)

    non_user_email = serializers.EmailField(max_length=50, required=False)
    user_email = serializers.IntegerField(read_only=True, required=False)

    def create(self, validated_data):
        with transaction.atomic():
            box = Box.objects.get(id=validated_data["box"])

            thread = Thread.objects.create(
                box = box,
                non_user_email = validated_data.get("non_user_email"), # kalau non-required field gini caranya
                user_email = validated_data.get("user_email")
            )

            message = Message.objects.create(
                message_title = validated_data.get("message_title"),
                message_body = validated_data["message_body"],
                thread = thread
            )
        
        return message
    
    def update(self, instance, validated_data):
        return instance