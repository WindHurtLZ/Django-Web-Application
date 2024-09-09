from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url="/login/")
def index(request):
    return render(request, 'home/index.html')

def device(request):
    return render(request, 'home/device.html')