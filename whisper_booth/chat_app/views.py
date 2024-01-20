from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.shortcuts import render, redirect
from django.utils import timezone
from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy

from .models import Message, AITranscript
from .forms import MessageFileForm

from ai_chat.chat_with_gpt import get_gpt_response_from_prompt

DEFAULT_AI_USERNAME = "HAL9000"

def index(request):
    if not request.user.is_authenticated:
        return redirect("login")
    
    return render(request, "chat_app/index.html", context={})

def messages(request):
    if not request.user.is_authenticated:
        return redirect("login")
    
    last_10_messages = Message.objects.filter(by_user=request.user).order_by("at_time")[:10]
    last_10_ai_messages = AITranscript.objects.filter(to_user=request.user).order_by("at_time")[:10]
    messages = []
    for message in last_10_messages:
        messages.append(
            {"text": message.text, "at_time": message.at_time, "by_user": message.by_user.username}
        )
    for message in last_10_ai_messages:
        messages.append(
            {"text": message.text, "at_time": message.at_time, "by_user": DEFAULT_AI_USERNAME}
        )

    messages.sort(key=lambda message: message["at_time"])

    context = {
        "messages": messages,
    }
    
    return render(request, "chat_app/messages.html", context)


def send_message(request):
    if request.method != "POST":
        return HttpResponse('Request should be POST.')

    text = request.POST.get('chat-msg', None)
    if text is not None and text != '':
        new_message = Message(text=text, by_user=request.user, at_time=timezone.now())
        new_message.save()

        gpt_response = get_gpt_response_from_prompt(text)
        new_transcript = AITranscript(text=gpt_response, to_user=request.user, at_time=timezone.now())
        new_transcript.save()

    return redirect('chat_app:messages')

class CreateFileUploadView(CreateView):  # new
    model = Message
    form_class = MessageFileForm
    template_name = "file_upload.html"
    success_url = reverse_lazy("home")