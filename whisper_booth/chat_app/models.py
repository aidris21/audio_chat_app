from django.db import models


class User(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)


class Message(models.Model):
    text = models.TextField(max_length=500)
    by_user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    at_time = models.DateTimeField("message time")
