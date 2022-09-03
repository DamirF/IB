from django import forms
from django.contrib.auth.models import User


class RegisterNewUser(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'username', 'password', ]
        wigets = {
            'password': forms.PasswordInput()
        }
