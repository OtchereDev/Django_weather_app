import os 
import requests
import datetime


apikey=os.getenv('ACCUWEATHER_APIKEY')


def getLocationDet(city):

    response=requests.get(f'http://dataservice.accuweather.com/locations/v1/cities/search?apikey={apikey}&q={city}')

    return response.json()[0] if response.json() else None



def getTemperatureDet(locationKey):

    temp_response=requests.get(f'http://dataservice.accuweather.com/currentconditions/v1/{locationKey}?apikey={apikey}')

    return temp_response.json()


def getName_LocKey(locationDet):

    return locationDet['EnglishName'],locationDet['Key']


def getForecastDet(locKey):

    response = requests.get(f'http://dataservice.accuweather.com/forecasts/v1/daily/5day/{locKey}?apikey={apikey}')

    result=response.json()

    temperatureCont=result['DailyForecasts']

    temperatureValues=[]
    
    
    for i in temperatureCont:
        date=datetime.datetime.fromisoformat(i['Date'])
        
        current_temp={
            'day':date.strftime('%A'),
            'min_temp':i['Temperature']['Minimum']['Value'],
            'max_temp':i['Temperature']['Maximum']['Value'],
            
        }

        temperatureValues.append(current_temp)

    return temperatureValues

