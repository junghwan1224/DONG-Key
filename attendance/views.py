from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from club.models import Club
from .models import Event
from .forms import EventForm


def event_list(request, pk):
    club = get_object_or_404(Club, pk=pk)
    ctx = {
            'club': club,
            'event_list': club.event_set.all(),
    }
    return render(request, 'attendance/event_list.html', ctx)


def create_event(request, pk):
    club = get_object_or_404(Club, pk=pk)
    if request.method == "POST":
        event_form = EventForm(club, request.POST)
        if event_form.is_valid():
            event = event_form.save(commit=False)
            event.club = club
            event.save()
            event_form.save_m2m()
            return redirect(reverse('attendance:read_event', kwargs={'event_pk': event.pk, }))
    else:
        event_form = EventForm(club)
    ctx = {
            'club': club,
            'event_form': event_form,
    }
    return render(request, 'attendance/create_event.html', ctx)


def read_event(request, event_pk):
    event = get_object_or_404(Event, pk=event_pk)
    club = event.club
    ctx = {
            'club': club,
            'event': event,
     }
    return render(request, 'attendance/read_event.html', ctx)
