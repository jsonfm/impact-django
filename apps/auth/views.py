from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class LoginView(TemplateView):
    template_name = 'auth/login.html'
    redirect_field_name = 'feed'

    
class SignupView(TemplateView):
    template_name = 'auth/signup.html'
    redirect_field_name = 'feed'