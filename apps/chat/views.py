from django.views.generic import TemplateView


class ChatIndexView(TemplateView):
    template_name = "chat/index.html"
