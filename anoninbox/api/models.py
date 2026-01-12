from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Box(models.Model):
    box_title = models.CharField(max_length=50)
    box_description = models.CharField(max_length=200, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    box_maker = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.box_title

class Message(models.Model):
    message_title = models.CharField(max_length=50, blank=True)
    message_body = models.CharField(max_length=1000)

    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    message_author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    message_box = models.ForeignKey(Box, on_delete=models.CASCADE)

    def __str__(self):
        return self.message_title

class Reply(models.Model):
    reply_message = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True, auto_now=False, blank=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True)

    message_replied = models.ForeignKey(Message, on_delete=models.CASCADE)

    def __str__(self):
        return self.reply_message
    