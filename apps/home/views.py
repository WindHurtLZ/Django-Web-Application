import json

from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from apps.management.models import Device


# Create your views here.
@login_required(login_url="/login/")
def home(request):
    return render(request, 'home/home.html')

@login_required(login_url="/login/")
def ride1_view(request):
    return render(request, 'home/ride-1.html')

def ride2_view(request):
    if not request.session.get('bike_verified'):
        return redirect('home')
    return render(request, 'home/ride-2.html')

def ride3_view(request):
    if not request.session.get('bike_verified'):
        return redirect('home')

    request.session.pop('bike_verified', None)
    return render(request, 'home/ride-3.html')

def validate_bike_number(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        bike_number = data.get('bike_number')

        try:
            Device.objects.get(asset_number=bike_number)
            # Session flag
            request.session['bike_verified'] = True
            return JsonResponse({'valid': True})
        except Device.DoesNotExist:
            return JsonResponse({'valid': False})

    return JsonResponse({'valid': False})

