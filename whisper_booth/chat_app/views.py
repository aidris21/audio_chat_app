from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.utils import timezone

from .models import Message

def index(request):
    if not request.user.is_authenticated:
        return redirect("login")
    
    return HttpResponse(f"Welcome to the Whisper Booth {request.user.username}!")

def messages(request):
    if not request.user.is_authenticated:
        return redirect("login")
    last_10_messages = Message.objects.filter(by_user=request.user).order_by("at_time")[:10]
    context = {
        "messages": last_10_messages,
    }
    
    return render(request, "chat_app/messages.html", context)


def send_message(request):
    if request.method == "POST":
        print(request.POST.keys())
        text = request.POST.get('chat-msg', None)
        if text is not None and text != '':
            new_message = Message(text=text, by_user=request.user, at_time=timezone.now())
            new_message.save()
        return redirect('chat_app:messages')
    else:
        return HttpResponse('Request should be POST.')

