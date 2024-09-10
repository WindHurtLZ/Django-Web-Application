from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from apps.home.forms import DeviceForm
from apps.home.models import Device


# Create your views here.

@login_required(login_url="/login/")
def index(request):

    form = DeviceForm()
    user_devices = Device.objects.filter(owner=request.user)
    context = {'devices': user_devices, 'form': form}

    return render(request, 'home/index.html', context)

@login_required(login_url="/login/")
def device(request):

    form = DeviceForm()
    user_devices = Device.objects.filter(owner=request.user)
    context = {'devices': user_devices, 'form': form}

    return render(request, 'home/device.html', context)


@login_required(login_url="/login/")
def add_device(request):
    if request.method == 'POST':
        form = DeviceForm(request.POST)
        if form.is_valid():
            new_device = form.save(commit=False)
            new_device.owner = request.user  # Set the owner to the current user
            new_device.save()
            return redirect('device')  # Redirect to the device list after saving
    else:
        form = DeviceForm()

    return render(request, 'home/device.html', {'form': form})