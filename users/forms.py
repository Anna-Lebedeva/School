from django.contrib.auth.forms import AuthenticationForm as DjangoAuthenticationForm
from django.contrib.auth.models import User


class AuthenticationForm(DjangoAuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
