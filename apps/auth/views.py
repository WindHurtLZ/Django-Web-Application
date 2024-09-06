from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm, RegisterForm

# Create your views here.
def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    # GET method
    return render(request, "accounts/login.html", {"form": form, "msg": msg})


def register_view(request):
    form = RegisterForm(request.POST or None)
    msg = None
    success = False

    if request.method == "POST":

        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            raw_password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=raw_password)

            msg = 'User created - please <a href="/login">login</a>.'
            success = True

            # return redirect("/login/")
        else:
            msg = 'Form is not valid'

    # GET Method
    return render(request, "accounts/register.html", {"form": form, "msg": msg, "success": success})
