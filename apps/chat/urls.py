from django.urls import path
from apps.chat.views import ChatIndexView, ChatRoomView


urlpatterns = [
    path(
        route='',
        view=ChatIndexView.as_view(),
        name="chat-index"
    ),    
    path(
        route='room',
        view=ChatRoomView.as_view(),
        name="chat-room"
    ),    
]