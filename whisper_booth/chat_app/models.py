from django.db import models


class User(models.Model):
    email = models.EmailField()
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Message(models.Model):
    text = models.TextField(max_length=500)
    by_user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    at_time = models.DateTimeField("message time")

    def __str__(self):
        return f"{self.text[0:50]}..."
