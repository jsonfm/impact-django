"""
ASGI config for impact project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter  # noqa isort:skip
from apps.chat.urls import urlpatterns as chat_urlpatterns
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'impact.settings')


application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": URLRouter(chat_urlpatterns),
    }
)
