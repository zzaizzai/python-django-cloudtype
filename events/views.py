from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Event


def all_events(requests):
    event_list = Event.objects.all()

    return render(requests, 'event_list.html',
                  {
                      'event_list': event_list
                  })


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
