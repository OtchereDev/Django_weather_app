from django.shortcuts import render

import requests
import os

from .forms import searchForm


def home(request):
    form=searchForm(request.POST or None)

    apikey=os.getenv('ACCUWEATHER_APIKEY')

    respone=requests.get(f'http://dataservice.accuweather.com/locations/v1/cities/search?apikey={apikey}&q=accra',)

    result=respone.json()[0]

    name,locKey=result['EnglishName'],result['Key']

    temp_response=requests.get(f'http://dataservice.accuweather.com/currentconditions/v1/{locKey}?apikey={apikey}')

    temp_result=temp_response.json()

    context={
        'city_name':name,
        'is_day':temp_result[0]['IsDayTime'],
        'temperature':temp_result[0]['Temperature']['Metric']['Value']
    }

    if form.is_valid():
        print('yes',request.POST.get('location'))
    else:
        print('no')

    return render(request,'weather_app/index.html',context)