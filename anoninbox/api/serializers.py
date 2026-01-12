from rest_framework import serializers

from .models import *

class BoxSerializer(serializers.ModelSerializer):
    box_maker = serializers.ReadOnlyField(source="box_maker_id")
    
    class Meta:
        model = Box
        fields = '__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = '__all__'

class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = '__all__'