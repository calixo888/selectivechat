from django.conf.urls import url
from . import views

urlpatterns = [
    url("^$", views.index, name="index"),
    url("^create-chat/$", views.create_chat, name="create_chat"),
    url("^join-chat/$", views.join_chat, name="join_chat"),
    url('^chat/(?P<chat_id>.+?)/$', views.chat, name='chat'),
]
