from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
@login_required(login_url="/login/")
def device_map(request):

    return render(request, 'widgets/map.html')