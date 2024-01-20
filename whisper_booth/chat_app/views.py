from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import Message

def index(request):
    return HttpResponse("Hello, world. You're at the chat_app index.")

def messages(request):
    last_10_messages = Message.objects.order_by("at_time")[:10]
    context = {
        "last_10_messages": last_10_messages,
    }
    return render(request, "chat_app/index.html", context)
