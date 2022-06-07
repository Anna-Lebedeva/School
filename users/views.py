from django.contrib.auth.views import LogoutView as DjangoLogoutView
from django.contrib.auth.views import LoginView as DjangoLoginView

from users.forms import AuthenticationForm


class LogoutView(DjangoLogoutView):
    template_name = "index.html"


class LoginView(DjangoLoginView):
    authentication_form = AuthenticationForm
    template_name = 'index.html'

