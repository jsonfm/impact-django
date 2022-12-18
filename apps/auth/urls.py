from django.urls import path, include
from apps.auth.views import LoginView


urlpatterns = [
    path(
        route='login/',
        view=LoginView.as_view(),
        name="login"
    )
]
