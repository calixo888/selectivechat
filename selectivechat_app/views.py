from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.safestring import mark_safe
from . import models
import json
import random
import string

def generate_key(length):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))


def index(request):
    return render(request, "selectivechat_app/index.html")


def create_chat(request):
    if request.method == "POST":
        chat_name = request.POST.get("chat_name")

        chat_id = generate_key(10)

        models.ChatRoom.objects.create(chat_id=chat_id, chat_room_name=chat_name)

        return HttpResponseRedirect(f"/chat/{chat_id}/")

    return render(request, "selectivechat_app/create_chat.html")


def join_chat(request):
    if request.method == "POST":
        chat_id = request.POST.get("chat_id")

        if models.ChatRoom.objects.filter(chat_id=chat_id).exists():
            return HttpResponseRedirect(f"/chat/{chat_id}/")
        else:
            return HttpResponse("Invalid Chat Room ID")

    return render(request, "selectivechat_app/join_chat.html")


def chat(request, chat_id):
    if models.ChatRoom.objects.filter(chat_id=chat_id).exists():
        chat_room = models.ChatRoom.objects.get(chat_id=chat_id)
        if request.GET.get("display_name"):
            return render(request, "selectivechat_app/chat.html", context={
                "room_name_json": mark_safe(json.dumps(chat_id)),
                "display_name": request.GET.get("display_name"),
                "chat_name": chat_room.chat_room_name,
                "chat_id": chat_id,
            })
        else:
            if request.method == "POST":
                display_name = request.POST.get("display_name")
                return HttpResponseRedirect(f"/chat/{chat_id}/?display_name={display_name}")
            else:
                return render(request, "selectivechat_app/display_name.html", context={
                    "chat_name": chat_room.chat_room_name,
                })
    else:
        return HttpResponse("Invalid Chat Room")
