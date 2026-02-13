from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Box(models.Model):
    box_title = models.CharField(max_length=50)
    box_description = models.CharField(max_length=1000, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    box_maker = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.box_title
    
class Thread(models.Model):
    box = models.ForeignKey(Box, on_delete=models.CASCADE)
    user_email = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    non_user_email = models.EmailField(max_length=50, blank=True, null=True)

    def __str__(self):
        return f"Thread dari Box: {self.box}"

class Message(models.Model):
    message_title = models.CharField(max_length=50, blank=True, null=True)
    message_body = models.CharField(max_length=1000)

    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    thread = models.ForeignKey(Thread, on_delete=models.CASCADE, related_name="messages") # related name ini biar si message ini bisa diquery dari Thread

    is_author_box_maker = models.BooleanField(default=False)

    def __str__(self):
        return self.message_title
    