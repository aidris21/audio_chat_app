from django.urls import path

from . import views

app_name = "chat_app"
urlpatterns = [
    path("", views.index, name="index"),
    path("messages/", views.messages, name="messages"),
    path("send_message/", views.send_message, name="send_message")
]