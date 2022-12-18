from django.urls import path
from apps.auth.views import LoginView, SignupView


urlpatterns = [
    path(
        route='login/',
        view=LoginView.as_view(),
        name="login"
    ),
    path(
        route='signup/',
        view=SignupView.as_view(),
        name="signup"
    ),
]
