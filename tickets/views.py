from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

from .models import *


def index(request):
    plays_list = Play.objects.all()
    return render(request, 'tickets/index.html', {'plays_list':plays_list})


@login_required
def details(request, play_id):
    play = get_object_or_404(Play, pk=play_id)
    perf_set = Performance.objects.filter(play_id=play.id).order_by('perf_date')
    return render(request, 'tickets/details.html', {'play': play, 'perf_set': perf_set})

def register(request):
    if request.method == "POST":
        if not (User.objects.filter(username=request.POST['username']).exists() or User.objects.filter(email=request.POST['email']).exists()):
            user=User.objects.create_user(request.POST['username'],
                                          request.POST['email'],
                                          request.POST['password'])
            user.first_name=request.POST['firstname']
            user.last_name = request.POST['lastname']
            user.save()
            return redirect('tickets:login')
        else:
            return render(request, 'tickets/register.html', {'wrong' : True})
    return render(request, 'tickets/register.html')

def loginView(request):
    if request.method=='POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('tickets:index')
        else:
            return render(request,'tickets/login.html')
    else:
        return render(request,'tickets/login.html')

def buy(request, performance_id):
    performance = get_object_or_404(Performance, pk=performance_id)

def logoutView(request):
    logout(request)
    return redirect('tickets:index')