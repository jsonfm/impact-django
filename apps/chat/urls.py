from django.urls import path
from apps.chat.views import ChatIndexView


urlpatterns = [
    path(
        route='',
        view=ChatIndexView.as_view(),
        name="chat-index"
    ),    
]