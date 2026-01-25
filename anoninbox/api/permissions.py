from rest_framework.permissions import BasePermission
from .models import Box, Thread


class IsBoxOwner(BasePermission):

    def has_permission(self, request, view):
        try:
            box = Box.objects.get(id=view.kwargs.get("box_id"))
            box_owner = box.box_maker

            return box_owner == request.user
            
        except:
            pass
            
        return False

class IsBoxOfThreadOwner(BasePermission):

    def has_permission(self, request, view):
        # Apakah user yg didapat dari cookies itu sama dengan user yg didapat dari box_maker of <int: box_id>?
        box_id_url = view.kwargs.get("box_id") # .get ini return pasti single instance (kalau .filter QuerySet) tapi sayangnya ngeraise error

        try:
            box = Box.objects.get(id=box_id_url)
            owner = box.box_maker

            return owner == request.user

        except:
            pass

        return False

class IsThreadMember(BasePermission):
    # apakah user yg didapat dari request == user_email thread | box_maker box
    def has_permission(self, request, view):
        user_requested = request.user
        
        try:
            box = Box.objects.get(id=view.kwargs.get("box_id"))
            box_owner = box.box_maker

            thread = Thread.objects.get(id=view.kwargs.get("thread_id"))
            thread_starter = thread.user_email

        except:
            return False

        return user_requested == box_owner or user_requested == thread_starter

