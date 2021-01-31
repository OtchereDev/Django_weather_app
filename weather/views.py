from django.shortcuts import render

import requests
import os

from .forms import searchForm
from .helpers import getLocationDet,getTemperatureDet,getName_LocKey,getForecastDet


def home(request):
    form=searchForm(request.POST or None)

    context={}

    if form.is_valid():
        locationDet=getLocationDet(request.POST.get('location'))

        if locationDet:

            name,locKey=getName_LocKey(locationDet)

            temperatureDet=getTemperatureDet(locKey)

            context={
                'city_name':name,
                'is_day':temperatureDet[0]['IsDayTime'],
                'temperature':temperatureDet[0]['Temperature']['Metric']['Value']
            }

    

    return render(request,'weather_app/index.html',context)


def forecast(request):
    form =searchForm(request.POST or None)

    context={}

    city=request.POST.get('location')or 'accra'

    if form.is_valid():
        name,locKey=getName_LocKey( getLocationDet(city))
        
        if locKey:
            currTemp=getTemperatureDet(locKey)
            forecastTemp=getForecastDet(locKey)
            context={
                'city_name':name,
                'is_day':currTemp[0]['IsDayTime'],
                'temperature':currTemp[0]['Temperature']['Metric']['Value'],
                'forecast_detail':forecastTemp[1:],
            }

            print(context)

    return render(request,'weather_app/forecast.html',context)