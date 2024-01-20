from django.db import models
from django.contrib.auth.models import User


class Message(models.Model):
    text = models.TextField(max_length=500)
    by_user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='by_user')
    at_time = models.DateTimeField("message time")

    def __str__(self):
        cutoff_length = 50
        end_text = "..." if len(self.text) > cutoff_length else ""
        return f"{self.text[0:50]}{end_text}"