from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

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
        return [IsAuthenticated(), IsOwner()]








