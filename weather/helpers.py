import os 
import requests


apikey=os.getenv('ACCUWEATHER_APIKEY')


def getLocationDet(city):

    respone=requests.get(f'http://dataservice.accuweather.com/locations/v1/cities/search?apikey={apikey}&q={city}')

    # return bool(respone.json())

    return respone.json()[0] if respone.json() else None



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
        current_temp={
            'min_temp':i['Temperature']['Minimum']['Value'],
            'max_temp':i['Temperature']['Maximum']['Value'],
            
        }

        temperatureValues.append(current_temp)

    return temperatureValues

