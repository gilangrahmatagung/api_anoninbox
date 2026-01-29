from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics, viewsets
from django.db import transaction

from .permissions import *
from .models import *
from .serializers import *


class AuthTestView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({"Kamu otentik!": f"Hai {request.user.email}!"})
    
class BoxListCreateView(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = BoxSerializer
    
    def perform_create(self, serializer):
        serializer.save(box_maker=self.request.user)

    def get_queryset(self):
        if self.request.method == "POST":
            return Box.objects.all()
        elif self.request.method == "GET":
            return Box.objects.filter(box_maker=self.request.user)

class BoxRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):    
    queryset = Box.objects.all()
    serializer_class = BoxSerializer

    def get_permissions(self):
        if self.request.method == "GET":
            return [AllowAny()]
        return [IsAuthenticated(), IsBoxOwner()]

# Thread and Messages & Start Thread
class ThreadListCreateView(generics.ListCreateAPIView):

    def get_permissions(self):
        if self.request.method == "POST":
            return [AllowAny()]
        return [IsAuthenticated(), IsBoxOfThreadOwner()]

    def get_serializer_class(self):
        if self.request.method == "POST":
            return StartThreadSerializer
        return ThreadAndMessagesSerializer

    # Thread and messages
    def get_queryset(self):
        if self.request.method == "GET":
            box_id = self.kwargs.get('box_id')
            return Thread.objects.filter(box=box_id)
        return super().get_queryset()
    
    # Start Thread
    @transaction.atomic
    def perform_create(self, serializer):
        if self.request.user.id is not None:
            user_email = self.request.user
        
        thread = Thread.objects.create(
                    box_id=self.kwargs.get("box_id"),
                    user_email=user_email if user_email else None,
                    non_user_email=serializer.validated_data.get("non_user_email")
                )
        
        Message.objects.create(
            thread = thread,
            message_title=serializer.validated_data.get("message_title"),
            message_body=serializer.validated_data["message_body"]
        )

class SendMessageView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated, IsThreadMember]
    serializer_class = MessageSerializer

    def perform_create(self, serializer):
        serializer.save(thread_id=self.kwargs.get("thread_id"))











