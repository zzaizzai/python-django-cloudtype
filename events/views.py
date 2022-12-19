from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Event, Venue
from .forms import VenueForm, EventForm
from django.core.paginator import Paginator


def venue_text(request):
    responce = HttpResponse(content_type='text/plain')
    responce['Content_Disposition'] = 'attachment; filename=venues.txt'

    venues = Venue.objects.all()

    lines = []
    for venue in venues:
        lines.append(f'{venue.name}\n{venue.address}\n{venue.phone}\n\n\n')

    responce.writelines(lines)

    return responce


def delete_event(request, event_id):
    event = Event.objects.get(pk=event_id)
    event.delete()
    return redirect('list_events')


def delete_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    venue.delete()
    return redirect('list_venues')


def all_events(requests):
    event_list = Event.objects.all().order_by('event_date')
    return render(requests, 'event_list.html',
                  {
                      'event_list': event_list
                  })


def update_venue(request, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    form = VenueForm(request.POST or None, instance=venue)

    if form.is_valid():
        form.save()
        return redirect('/events/list_venues')
    return render(request, "update_venue.html",
                  {"venue": venue,
                   "form": form})


def update_event(request, event_id):

    event = Event.objects.get(pk=event_id)

    form = EventForm(request.POST or None, instance=event)

    if form.is_valid():
        form.save()
        return redirect('/events/list_events')
    return render(request, "update_event.html",
                  {"event": event,
                   "form": form})


def search_venues(request):
    if request.method == "POST":

        searched = request.POST["searched"]
        venues = Venue.objects.filter(name__contains=searched)
        return render(request, "search_venues.html",
                      {"searched": searched,
                       "venues": venues})
    else:
        return render(request, "search_venues.html",
                      {})


def show_venue(requests, venue_id):
    venue = Venue.objects.get(pk=venue_id)
    print(venue)
    return render(requests, "show_venue.html",
                  {'venue': venue})


def list_venues(request):
    # venue_list = Venue.objects.all().order_by('name')

    p = Paginator(Venue.objects.all(), 2)
    page = request.GET.get('page')
    venues = p.get_page(page)

    nums = "a" * venues.paginator.num_pages

    return render(request, 'list_venues.html',
                  {
                      #   "venue_list": venue_list,
                      "venues": venues,
                      "nums": nums
                  })


def add_event(request):
    submitted = False

    if request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/events/add_event?sumitted=True')
    else:
        form = EventForm
        if 'sumitted' in request.GET:
            submitted = True

    form = EventForm
    return render(request, 'add_event.html', {'form': form, 'submitted': submitted})


def add_venue(requests):
    submitted = False

    if requests.method == "POST":
        form = VenueForm(requests.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/events/add_venue?sumitted=True')
    else:
        form = VenueForm
        if 'sumitted' in requests.GET:
            submitted = True

    form = VenueForm
    return render(requests, 'add_venue.html', {'form': form, 'submitted': submitted})


def home(requests, year=datetime.now().year, month=datetime.now().strftime('%B')):

    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)

    cal = HTMLCalendar().formatmonth(year, month_number)

    now = datetime.now()
    current_year = now.year
    current_month = now.month
    time = now.strftime('%I:%M %p')

    return render(requests, 'home.html',
                  {
                      "year": year,
                      "month": month,
                      "month_number": month_number,
                      "cal": cal,
                      "current_year": current_year,
                      "current_month": current_month,
                      "time": time
                  })
