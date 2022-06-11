from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import *


@login_required(login_url='login:login')
def index(request):
    return render(request, 'camera/camera_main.html')
