from django.views.generic import TemplateView


class LoginView(TemplateView):
    template_name = 'auth/login.html'


class SignupView(TemplateView):
    template_name = 'auth/signup.html'