from django.shortcuts import render

import requests
import os

from .forms import searchForm
from .helpers import getLocationDet,getTemperatureDet,getName_LocKey,getForecastDet,getForecastWeather,getCurrentWeather


def home(request):
    form=searchForm(request.POST or None)

    context=getCurrentWeather(request)

    if form.is_valid():
        context=getCurrentWeather(request)

    return render(request,'weather_app/index.html',context)


def forecast(request):
    form =searchForm(request.POST or None)

    context=getForecastWeather(request)

    if form.is_valid():
        context=getForecastWeather(request)

    return render(request,'weather_app/forecast.html',context)