from django.conf.urls import url
from . import views

urlpatterns = [
    url("^$", views.index, name="index"),
    url('^chat/(?P<chat_id>.+?)/$', views.chat, name='chat'),
]
