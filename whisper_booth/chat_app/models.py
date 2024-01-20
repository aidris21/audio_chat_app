from django.db import models
from django.contrib.auth.models import User

def text_summary(text: str):
    cutoff_length = 50
    end_text = "..." if len(text) > cutoff_length else ""
    return f"{text[0:50]}{end_text}"


class Message(models.Model):
    text = models.TextField(max_length=500, null=True)
    file = models.FileField(null=True)
    by_user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='by_user')
    at_time = models.DateTimeField("message time")

    def __str__(self):
        return text_summary(self.text)
    

class AITranscript(models.Model):
    text = models.TextField(max_length=500, null=True)
    to_user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='to_user')
    at_time = models.DateTimeField()

    def __str__(self):
        return text_summary(self.text)