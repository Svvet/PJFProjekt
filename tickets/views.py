from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic

from .models import *


class IndexView(generic.ListView):
    template_name = 'tickets/index.html'
    context_object_name = 'plays_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Play.objects.order_by('-title')

def details(request, play_id):
    play = get_object_or_404(Play, pk=play_id)
    perf_set = Performance.objects.filter(play_id=play.id).order_by('perf_date')
    return render(request, 'tickets/details.html', {'play': play, 'perf_set': perf_set})

def buy(request, performance_id):
    performance = get_object_or_404(Performance, pk=performance_id)
