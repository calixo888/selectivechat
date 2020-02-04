from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.utils.safestring import mark_safe
import json

def index(request):
    return render(request, "selectivechat_app/index.html")


def chat(request, chat_id):
    if request.GET.get("display_name"):
        return render(request, "selectivechat_app/chat.html", context={
            "room_name_json": mark_safe(json.dumps(chat_id)),
            "display_name": request.GET.get("display_name"),
        })
    else:
        if request.method == "POST":
            display_name = request.POST.get("display_name")
            return HttpResponseRedirect(f"/chat/{chat_id}/?display_name={display_name}")
        else:
            return render(request, "selectivechat_app/display_name.html")
