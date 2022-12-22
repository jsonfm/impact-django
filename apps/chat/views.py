from django.views.generic import TemplateView


class ChatIndexView(TemplateView):
    template_name = "chat/index.html"


class ChatRoomView(TemplateView):
    template_name = "chat/room.html"
