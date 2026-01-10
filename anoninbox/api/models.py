from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class Box(models.Model):
    box_title = models.CharField(max_length=50)
    box_description = models.CharField(max_length=200)

    box_starter = models.ForeignKey(User)

class Message(models.Model):
    message_title = models.CharField(max_length=50)
    message_body = models.CharField(max_length=1000)

    message_author = models.ForeignKey(User)
    message_box = models.ForeignKey(Box)

class Reply(models.Model):
    reply_message = models.CharField(max_length=200)

    message_replied = models.ForeignKey(Message)
    