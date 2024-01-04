from django.shortcuts import render

from django.http import HttpResponse
import datetime
from django.utils import timezone
import random


def HomePage(request):
    now = datetime.datetime.now()
    now_tz = timezone.now()

    l = ['شنبه' , 'یک شنبه ' , 'دو شنبه' , 'سه شنبه']

    r = random.choice(l)
    x = random.randint(1, 12000)

    return render(
        request,
        'home/home.html',
        {
            'html_date_time': now,
            'time_tz': now_tz,
            'r': r,
        }
    )

def About(request):
    return render(
        request,
        'home/about_us.html'
    )
