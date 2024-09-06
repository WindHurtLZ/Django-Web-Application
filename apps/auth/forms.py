from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "id": "email",
                "placeholder": "Username",
                "class": "form-input w-full",
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "id": "password",
                "placeholder": "Password",
                "class": "form-input w-full",
                "autocomplete": 'on',
            }
        ))


class RegisterForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "id": "name",
                "placeholder": "Username",
                "class": "form-input w-full",
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "id": "email",
                "placeholder": "Email",
                "class": "form-input w-full",
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "id": "password1",
                "placeholder": "Password",
                "class": "form-input w-full",
                "autocomplete": 'on',
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "id": "password2",
                "placeholder": "Password check",
                "class": "form-input w-full",
                "autocomplete": 'on',
            }
        ))

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
