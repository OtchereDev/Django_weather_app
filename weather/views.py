from django.shortcuts import render

import requests
import os

from .forms import searchForm
from .helpers import getLocationDet,getTemperatureDet


def home(request):
    form=searchForm(request.POST or None)

    context={}

    if form.is_valid():
        locationDet=getLocationDet(request.POST.get('location'))

        if locationDet:

            name,locKey=locationDet['EnglishName'],locationDet['Key']

            temperatureDet=getTemperatureDet(locKey)

            context={
                'city_name':name,
                'is_day':temperatureDet[0]['IsDayTime'],
                'temperature':temperatureDet[0]['Temperature']['Metric']['Value']
            }

    

    return render(request,'weather_app/index.html',context)